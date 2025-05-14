from django.db import models

class ProblemReport(models.Model):
    PROBLEM_TYPES = [
        ('infrastructure', 'Infrastructure'),
        ('environment', 'Environment'),
        ('safety', 'Safety'),
        ('health', 'Health'),
        ('other', 'Other'),
    ]

    problem_type = models.CharField(max_length=20, choices=PROBLEM_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_problem_type_display()} - {self.location}"

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title