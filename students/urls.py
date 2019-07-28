from django.urls import path, include
from . views import students

urlpatterns = [
    path('<int:c_name>/', students, name="students"),
]
