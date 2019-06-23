from django.shortcuts import render
from . models import Staff

def staff_list(request):
    my_staff = Staff.objects.all()
    context = {
        "my_staff" : my_staff,
    }
    return render(request, 'table.html', context )
