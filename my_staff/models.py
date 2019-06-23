from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Staff(models.Model):
    STAFF_CHOICES = [
        ('Teacher', 'teacher'),
        ('Support Staff', 'Support Staff'),
    ]

    GENDER = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('undisclose', 'UNDISCLOSE')
    ]

    staff_image = models.ImageField(upload_to="images/")
    sur_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_designation = models.CharField(max_length=20, choices=STAFF_CHOICES, default='Teacher')
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    email_address = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.sur_name

    class Meta:
        ordering = ('sur_name', 'staff_designation',)
