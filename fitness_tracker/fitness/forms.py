from django import forms
from .models import Activity, Goal

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'duration', 'distance', 'calories_burned', 'date']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description', 'target_date']
