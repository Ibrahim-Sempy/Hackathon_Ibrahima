from django.test import TestCase
from .models import Route, PointOfInterest

class NavigationModelTests(TestCase):

    def setUp(self):
        Route.objects.create(name="Route 1", description="Main route through the city")
        PointOfInterest.objects.create(name="Park", description="A nice park in the city", location="City Center")

    def test_route_creation(self):
        route = Route.objects.get(name="Route 1")
        self.assertEqual(route.description, "Main route through the city")

    def test_point_of_interest_creation(self):
        poi = PointOfInterest.objects.get(name="Park")
        self.assertEqual(poi.description, "A nice park in the city")