from django.db import models


class Col(models.Model):
    rank = models.IntegerField()
    state = models.CharField(max_length=64)
    index = models.DecimalField(max_digits=5, decimal_places=1)
    grocery = models.DecimalField(max_digits=5, decimal_places=1)
    housing = models.DecimalField(max_digits=5, decimal_places=1)
    utilities = models.DecimalField(max_digits=5, decimal_places=1)
    transportation = models.DecimalField(max_digits=5, decimal_places=1)
    health = models.DecimalField(max_digits=5, decimal_places=1)
    misc = models.DecimalField(max_digits=5, decimal_places=1)
    state_code = models.CharField(max_length=10)

    def __str__(self):
        return self.state
