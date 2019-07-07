from django.urls import path, include
from . views import all_parents

urlpatterns = [
    path('', all_parents, name="parents"),
]

