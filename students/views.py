from django.shortcuts import render
from . models import My_Students

# Create your views here.

def students(request, c_name):
    my_class = My_Students.objects.filter(student_class__pk=c_name)
    if my_class:
        context = {
            'students':my_class
        }
    else:
        context = {
            'student':'No Student in this class'
        }
    return render(request, 'students/index.html', context)

