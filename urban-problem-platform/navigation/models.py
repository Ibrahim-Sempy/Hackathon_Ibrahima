from django.db import models

class PointOfInterest(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    # location = models.PointField()  # Removed for SQLite compatibility
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Route(models.Model):
    start_point = models.ForeignKey(PointOfInterest, related_name='start_routes', on_delete=models.CASCADE)
    end_point = models.ForeignKey(PointOfInterest, related_name='end_routes', on_delete=models.CASCADE)
    distance = models.FloatField()
    estimated_time = models.DurationField()

    def __str__(self):
        return f"Route from {self.start_point} to {self.end_point}"

class Alert(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert at {self.point_of_interest}: {self.message}"