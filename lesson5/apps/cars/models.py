from django.db import models
from django.db.models import ForeignKey

from apps.auto_parks.models import AutoParkModel
from core.models import CoreModel


class CarModel(CoreModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=24)
    year = models.IntegerField()
    body_type = models.CharField(max_length=18)
    seats = models.IntegerField()
    volume = models.FloatField(default=0.0)
    auto_park = ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
