from django.urls import path

from apps.cars.views import CarListView, SingleCarView

urlpatterns = [
    path('', CarListView.as_view()),
    path('<int:pk>', SingleCarView.as_view())

]