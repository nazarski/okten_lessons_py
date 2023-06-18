from rest_framework import serializers
from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'body_type', 'seats', 'volume', 'auto_park', 'created_at', 'updated_at',)


class CarGetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year',)


class CarAutoParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'body_type', 'seats', 'volume', 'created_at', 'updated_at',)
