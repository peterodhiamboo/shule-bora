from django.shortcuts import render
from . models import Staff

def teachers(request):
    my_staff = Staff.objects.filter(staff_designation='Teacher')
    context = {
        "my_staff" : my_staff,
    }
    return render(request, 'staff.html', context )

def non_teaching_staff(request):
    my_staff = Staff.objects.filter(staff_designation='Support Staff')
    context = {
        "my_staff" : my_staff,
    }
    return render(request, 'staff.html', context )