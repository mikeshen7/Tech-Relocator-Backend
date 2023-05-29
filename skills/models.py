from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


class Skill(models.Model):
    title = models.CharField(max_length=256)
    skills = ArrayField(models.CharField(max_length=128, blank=True), size=8)

    def __str__(self):
        return self.title
