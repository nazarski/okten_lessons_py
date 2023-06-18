from django.db import models

from core.models import CoreModel


# Create your models here.
class AutoParkModel(CoreModel):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=24)
