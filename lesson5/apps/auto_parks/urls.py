from django.urls import path

from apps.auto_parks.views import AutoParkListView, AutoParkListCreateCarView, AutoParkCreateUpdateDeleteView
from apps.cars.views import CarListView, SingleCarView

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>', AutoParkCreateUpdateDeleteView.as_view()),
    path('/<int:pk>/cars', AutoParkListCreateCarView.as_view()),

]