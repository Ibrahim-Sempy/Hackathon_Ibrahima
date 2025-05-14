from django import forms
from .models import Report
from .models import Comment

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['problem_type', 'description', 'photo', 'latitude', 'longitude']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']