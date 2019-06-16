from django.db import models

class Class_Layout(models.Model):
    class_name = models.CharField(max_length=20)
    designated_fee = models.IntegerField()
    class_teacher = models.ForeignKey()

    def __str__(self):
        return self.class_name

    class Meta:
        ordering = ('class_name', 'class_teacher',)
