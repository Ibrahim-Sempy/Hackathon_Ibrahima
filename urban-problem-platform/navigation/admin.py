from django.contrib import admin
from .models import Route, PointOfInterest, Alert

admin.site.register(Route)
admin.site.register(PointOfInterest)
admin.site.register(Alert)