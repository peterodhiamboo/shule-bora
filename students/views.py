from django.shortcuts import render
from . models import My_Students
from my_class.models import Class_Layout

# Create your views here.

def students(request):
    my_class = Class_Layout.objects.filter(class_name=my_class_name)
    # students = My_Students.objects.get(student_class=my_class)

    if students:                                                                                                    
        context = {
            'student': students,
        }
    else:
        context = {
            'student': 'No Student Here',
        }
    return render(request, 'students/index.html', context)
