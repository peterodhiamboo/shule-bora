from django.urls import path
from .views import teachers, non_teaching_staff

urlpatterns = [
    path('teachers/', teachers, name="teachers"),
    path('non-teachers/', non_teaching_staff, name="non-teachers")
]
