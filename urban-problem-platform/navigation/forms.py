from django import forms
from .models import Route, PointOfInterest

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'description', 'start_latitude', 'start_longitude', 'end_latitude', 'end_longitude']

class PointOfInterestForm(forms.ModelForm):
    class Meta:
        model = PointOfInterest
        fields = ['name', 'category', 'description', 'latitude', 'longitude']