from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class User_Profile(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    desired_location = models.CharField(max_length=64, blank=True)
    desired_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skills = models.CharField(max_length=64, blank=True)
    saved_locations = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.title
