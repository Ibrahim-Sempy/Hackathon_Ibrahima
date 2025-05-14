from django.db import models

class PointOfInterest(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    # location = models.PointField()  
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    end_latitude = models.FloatField()
    end_longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Alert(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert at {self.point_of_interest}: {self.message}"