
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from apps.cars.models import CarModel
from .filters import car_filter_queryset
from .serializers import CarSerializer


class CarListView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter_queryset(self.request.query_params)


class SingleCarView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
