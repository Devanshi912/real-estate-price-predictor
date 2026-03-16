from django import forms

class PredictionForm(forms.Form):
    area = forms.IntegerField(label='Area (sq ft)', min_value=1)

    location = forms.ChoiceField(
        choices=[
            ('Ahmedabad', 'Ahmedabad'),
            ('Surat', 'Surat'),
            ('Vadodara', 'Vadodara'),
            ('Rajkot', 'Rajkot'),
            ('Gandhinagar', 'Gandhinagar'),
            ('Bhavnagar', 'Bhavnagar'),
            ('Junagadh', 'Junagadh'),
            ('Anand', 'Anand'),
            ('Navsari', 'Navsari'),
            ('Mehsana', 'Mehsana'),
            ('Jamnagar', 'Jamnagar')
        ],
        label='Location'
    )

    bedrooms = forms.IntegerField(label='Bedrooms', min_value=1)
    bathrooms = forms.IntegerField(label='Bathrooms', min_value=1)
    year_built = forms.IntegerField(label='Year Built', min_value=1800, max_value=2100)

    parking = forms.BooleanField(label='Parking', required=False)
    garden = forms.BooleanField(label='Garden', required=False)
    pool = forms.BooleanField(label='Swimming Pool', required=False)
