import json

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from cars.models import CarModel
from django.http import Http404
from .serializers import CarSerializer, CarGetListSerializer


class CarListView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarGetListSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class SingleCarView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serialized_car = CarSerializer(car)
        return Response(serialized_car.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serialized_car = CarSerializer(car, data)
        serialized_car.is_valid(raise_exception=True)

        serialized_car.save()
        return Response(serialized_car.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serialized_car = CarSerializer(car, data, partial=True)
        serialized_car.is_valid(raise_exception=True)
        serialized_car.save()
        return Response(serialized_car.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()

        return Response('deleted', status.HTTP_204_NO_CONTENT)
