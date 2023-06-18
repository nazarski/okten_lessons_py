from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel
from apps.cars.serializers import CarGetListSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarGetListSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')

    name = serializers.CharField(max_length=24)
