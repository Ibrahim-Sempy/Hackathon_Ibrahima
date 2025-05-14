from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Route, PointOfInterest, Alert

def calculate_route(request):
    # Logic to calculate the best route based on user input
    # This is a placeholder for the actual implementation
    return JsonResponse({"message": "Route calculation not implemented."})

def list_points_of_interest(request):
    points = PointOfInterest.objects.all()
    return render(request, 'navigation/points_of_interest.html', {'points': points})

def display_alerts(request):
    alerts = Alert.objects.all()
    return render(request, 'navigation/alerts.html', {'alerts': alerts})

class RouteListView(ListView):
    model = Route
    template_name = 'navigation/route_list.html'  # Créez ce template ou adaptez le nom
    context_object_name = 'routes'

class RouteDetailView(DetailView):
    model = Route
    template_name = 'navigation/route_detail.html'  # Créez ce template ou adaptez le nom
    context_object_name = 'route'

class AlertListView(ListView):
    model = Alert
    template_name = 'navigation/alert_list.html'  # Créez ce template ou adaptez le nom
    context_object_name = 'alerts'

class PointOfInterestListView(ListView):
    model = PointOfInterest
    template_name = 'navigation/pointofinterest_list.html'  # Créez ce template ou adaptez le nom
    context_object_name = 'points'