from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=256)
    salary_high = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    salary_low = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    salary_avg = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    lat = models.DecimalField(max_digits=15, decimal_places=10)
    lon = models.DecimalField(max_digits=15, decimal_places=10)
    city = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=256, null=True, blank=True)
    state_code = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    months_experience = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    education = models.CharField(max_length=256, null=True, blank=True)
    employment_type = models.CharField(max_length=256, null=True, blank=True) # change to dropdown
    industry = models.CharField(max_length=256, null=True, blank=True)
    job_function = models.CharField(max_length=256, null=True, blank=True)
    senority = models.CharField(max_length=256, null=True, blank=True) # change to dropdown
    skills = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title
