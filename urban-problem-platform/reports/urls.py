from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('create/', views.report_create, name='report_create'),
    path('map/', views.report_map, name='report_map'),
    path('<int:pk>/', views.report_detail, name='report_detail'),
    path('<int:pk>/vote/', views.vote_report, name='vote_report'),
    path('stats/', views.report_stats, name='report_stats'),
]