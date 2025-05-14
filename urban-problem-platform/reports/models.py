from django.db import models
from django.contrib.auth.models import User
from navigation.models import Route

class Report(models.Model):
    PROBLEM_TYPES = [
        ('road', 'Route endommagée'),
        ('electricity', 'Panne électrique'),
        ('waste', 'Déchets sauvages'),
        ('sanitation', 'Problème d\'assainissement'),
        ('other', 'Autre incident'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports', null=True, blank=True)
    problem_type = models.CharField(max_length=20, choices=PROBLEM_TYPES, null=True, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='reports/photos/', blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='reports')
    status = models.CharField(max_length=20, choices=[('new', 'Nouveau'), ('in_progress', 'En cours'), ('resolved', 'Résolu')], default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_problem_type_display()} - {self.description[:30]}"

    class Meta:
        ordering = ['-created_at']

class Vote(models.Model):
    report = models.ForeignKey('Report', on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('report', 'user')

class Comment(models.Model):
    report = models.ForeignKey('Report', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)