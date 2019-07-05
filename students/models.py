from django.db import models
from my_class.models import Class_Layout


class My_Students(models.Model):
    GENDER = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    ]

    student_image = models.ImageField(upload_to="student_images/")
    sur_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ups_number = models.CharField(max_length=5)
    added_at = models.DateTimeField(auto_now_add=True)
    student_class = models.ForeignKey(Class_Layout, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.sur_name
