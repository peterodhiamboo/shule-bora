from django.db import models
from my_staff.models import Staff


class Class_Layout(models.Model):
    class_name = models.CharField(max_length=20)
    designated_fee = models.IntegerField()
    class_teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True,
                                      null=True)
    date_added = models.DateTimeField(blank=True)

    def __str__(self):
        return self.class_name

    class Meta:
        ordering = ('class_name', 'class_teacher',)
