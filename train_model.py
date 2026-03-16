
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('pricepredictor/data/real_estate_data.csv')


df = pd.get_dummies(df, columns=['location', 'property_type','furnishing_status'])


X = df.drop('price', axis=1)
y = df['price']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


knn_model = KNeighborsRegressor(n_neighbors=1) 
knn_model.fit(X_scaled, y)

# Save model, scaler, and training columns
import pickle, os

os.makedirs('predictor_model', exist_ok=True)
pickle.dump(knn_model, open('predictor_model/model.pkl', 'wb'))
pickle.dump(scaler, open('predictor_model/scaler.pkl', 'wb'))
pickle.dump(list(X.columns), open('predictor_model/train_columns.pkl', 'wb'))

print("✅ KNN model, scaler, and training columns saved.")


