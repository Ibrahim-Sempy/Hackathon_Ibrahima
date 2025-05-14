from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/', views.RouteDetailView.as_view(), name='route-detail'),
    path('alerts/', views.AlertListView.as_view(), name='alert-list'),
    path('points-of-interest/', views.PointOfInterestListView.as_view(), name='poi-list'),
]