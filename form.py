from django import forms

class PredictionForm(forms.Form):
    area = forms.FloatField(label='Area (sq ft)')
    bedrooms = forms.IntegerField(label='Number of Bedrooms')
