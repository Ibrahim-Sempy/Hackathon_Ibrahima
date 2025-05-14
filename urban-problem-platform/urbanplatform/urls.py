from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('navigation/', include('navigation.urls')),
]