from django.db import models


class ColCity(models.Model):
    index = models.DecimalField(max_digits=5, decimal_places=1)
    city = models.CharField(max_length=64)
    state_code = models.CharField(max_length=10)
    state = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city}, {self.state_code}'
