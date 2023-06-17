from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=24)
    year = models.IntegerField()
    body_type = models.CharField(max_length=18)
    seats = models.IntegerField()
    volume = models.FloatField()
