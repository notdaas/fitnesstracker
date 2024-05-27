
from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()
    distance = models.FloatField()
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} - {self.user.username}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    target_date = models.DateField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.description
