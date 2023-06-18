from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, CarAutoParkSerializer, CarGetListSerializer


# Create your views here.
class AutoParkListView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()


class AutoParkListCreateCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        if not AutoParkModel.objects.filter(pk=pk).exists():
            raise Http404()
        cars = CarModel.objects.filter(auto_park_id=pk)
        serializer = CarGetListSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = CarAutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        if not AutoParkModel.objects.filter(pk=pk).exists():
            raise Http404()
        serializer.save(auto_park_id=pk)

        return Response(serializer.data, status.HTTP_201_CREATED)


class AutoParkCreateUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
