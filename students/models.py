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

    def school_fee(self):
        return self.student_class.designated_fee
    
    def get_upi(self):
        return self.ups_number

class Fee(models.Model):
    student = models.CharField(max_length=5)
    amount_paid = models.IntegerField()
    paid_on = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(null=True, blank=True)

    # get amounts paid
    def compare(self):
        fee_list = []
        fees = Fee.objects.filter(student=self).values('amount_paid')

        for k, v in enumerate(fees):
            fee_list.append(v['amount_paid'])
        return sum(fee_list)

    def get_student(self):
        student = My_Students.objects.get(ups_number=self.student)
        return student.first_name

    def __str__(self):
        return self.student




