from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.RouteListView.as_view(), name='route-list'),
    path('routes/<int:pk>/', views.RouteDetailView.as_view(), name='route-detail'),
    path('alerts/', views.AlertListView.as_view(), name='alert-list'),
    path('points-of-interest/', views.PointOfInterestListView.as_view(), name='poi-list'),
    path('routes/', views.route_list, name='route_list'),
    path('routes/create/', views.route_create, name='route_create'),
    path('routes/<int:pk>/edit/', views.route_edit, name='route_edit'),
    path('routes/<int:pk>/reports/', views.route_reports, name='route_reports'),
    path('points-of-interest/', views.point_of_interest_list, name='points_of_interest'),
    path('points-of-interest/create/', views.pointofinterest_create, name='pointofinterest_create'),
    path('points-of-interest/<int:pk>/edit/', views.pointofinterest_edit, name='pointofinterest_edit'),
    path('points-of-interest/<int:pk>/delete/', views.pointofinterest_delete, name='pointofinterest_delete'),
]