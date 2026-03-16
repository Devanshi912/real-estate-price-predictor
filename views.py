from django.shortcuts import render, redirect
import pandas as pd
import pickle
import os
from .models import Property
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout



# Path setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'predictor_model', 'model.pkl')
COLUMNS_PATH = os.path.join(BASE_DIR, 'predictor_model', 'train_columns.pkl')

# Load model and columns
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

with open(COLUMNS_PATH, 'rb') as f:
    train_columns = pickle.load(f)

with open('predictor_model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def home(request):
    return render(request, 'home.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def logoutaccount(request):
    logout(request)
    return redirect('home') 

def price_predict(request):
    if request.method == 'POST':
        try:
            area = int(request.POST.get('area'))
            bedrooms = int(request.POST.get('bedrooms'))
            bathrooms = int(request.POST.get('bathrooms'))
            location = request.POST.get('location')
            year_built = int(request.POST.get('year_built'))
            amenities = request.POST.getlist('amenities')
            property_type = request.POST.get('property_type')

            # Create input dictionary
            input_data = {
                'area': area,
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'year_built': year_built,
                'parking': 1 if 'parking' in amenities else 0,
                'garden': 1 if 'garden' in amenities else 0,
                'pool': 1 if 'pool' in amenities else 0,
                f'location_{location}': 1,
                f'property_type_{property_type}': 1
            }

            # Create dataframe and ensure all expected columns exist
            input_df = pd.DataFrame([input_data])

            for col in train_columns:
                if col not in input_df.columns:
                    input_df[col] = 0

            input_df = input_df[train_columns]

            # Apply feature scaling before prediction (required for KNN)
            input_scaled = scaler.transform(input_df)

            # Predict
            predicted_price = model.predict(input_scaled)[0]

            # Store results in session for the result page
            request.session['prediction_data'] = {
                'predicted_price': int(predicted_price),
                'area': area,
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'location': location,
                'year_built': year_built,
                'property_type': property_type,
                'amenities': amenities,
            }

            return redirect('prediction_result')

        except Exception as e:
            print("Prediction error:", e)

    return render(request, 'price_predict.html')
def property_search(request):
    query = request.GET.get('q')
    if query:
        query = query.lower().replace("bhk", "").strip()
        properties = Property.objects.filter(
            Q(location__icontains=query) |
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(bedrooms__icontains=query)
        )
    else:
        properties = Property.objects.all() 

    return render(request, 'search_results.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property': property})

def prediction_result(request):
    data = request.session.get('prediction_data')

    if not data:
        return redirect('price_predict')

    return render(request, 'result.html', {'data': data})



def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'contact.html')

def property_listings(request):
    properties = Property.objects.all()
    return render(request, 'property_listings.html', {'properties': properties})