from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Route, PointOfInterest, Alert
from .forms import RouteForm, PointOfInterestForm
from reports.models import Report

def calculate_route(request):
    return JsonResponse({"message": "Route calculation not implemented."})

def list_points_of_interest(request):
    points = PointOfInterest.objects.all()
    return render(request, 'navigation/points_of_interest.html', {'points': points})

def display_alerts(request):
    alerts = Alert.objects.all()
    return render(request, 'navigation/alerts.html', {'alerts': alerts})

def route_list(request):
    query = request.GET.get('q', '')
    routes = Route.objects.all()
    if query:
        routes = routes.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    return render(request, 'navigation/route_list.html', {
        'routes': routes,
        'query': query,
    })

def route_create(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm()
    return render(request, 'navigation/route_form.html', {'form': form})

def route_edit(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'navigation/route_form.html', {'form': form, 'route': route})

def route_reports(request, pk):
    route = get_object_or_404(Route, pk=pk)
    reports = route.reports.all()
    return render(request, 'navigation/route_reports.html', {'route': route, 'reports': reports})

def point_of_interest_list(request):
    points = PointOfInterest.objects.all()
    query = request.GET.get('q', '')
    if query:
        points = points.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
    return render(request, 'navigation/points_of_interest.html', {'points': points, 'query': query})

def pointofinterest_create(request):
    if request.method == 'POST':
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('points_of_interest')
    else:
        form = PointOfInterestForm()
    return render(request, 'navigation/pointofinterest_form.html', {'form': form})

def pointofinterest_edit(request, pk):
    poi = get_object_or_404(PointOfInterest, pk=pk)
    if request.method == 'POST':
        form = PointOfInterestForm(request.POST, instance=poi)
        if form.is_valid():
            form.save()
            return redirect('points_of_interest')
    else:
        form = PointOfInterestForm(instance=poi)
    return render(request, 'navigation/pointofinterest_form.html', {'form': form, 'poi': poi})

def pointofinterest_delete(request, pk):
    poi = get_object_or_404(PointOfInterest, pk=pk)
    if request.method == 'POST':
        poi.delete()
        return redirect('points_of_interest')
    return render(request, 'navigation/pointofinterest_confirm_delete.html', {'poi': poi})

class RouteListView(ListView):
    model = Route
    template_name = 'navigation/route_list.html' 
    context_object_name = 'routes'

class RouteDetailView(DetailView):
    model = Route
    template_name = 'navigation/route_detail.html' 
    context_object_name = 'route'

class AlertListView(ListView):
    model = Alert
    template_name = 'navigation/alert_list.html'  
    context_object_name = 'alerts'

class PointOfInterestListView(ListView):
    model = PointOfInterest
    template_name = 'navigation/pointofinterest_list.html'  
    context_object_name = 'points'