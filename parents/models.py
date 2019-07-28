from django.db import models
from students.models import My_Students
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Parents(models.Model):
    student = models.ForeignKey(My_Students, on_delete=models.CASCADE, null=False, blank=False)
    full_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(blank=False, null=False)
    email_address = models.EmailField(max_length=70,blank=True)


    def parent_name(self):
        return self.full_name
