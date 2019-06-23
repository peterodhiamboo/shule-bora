from django.urls import path
from .views import staff_list

urlpatterns = [
    path('staff/', staff_list, name="my_staff"),
]
