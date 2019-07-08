from django.shortcuts import render
from my_class.models import Class_Layout
from students.models import My_Students
from django.http import JsonResponse

my_classes = Class_Layout.objects.all().order_by('date_added')

context = {
    'classes': my_classes,
}

def homepage(request):
    return render(request, 'goldentouch/index.html', context )

def accounts(request):
    return render(request, 'goldentouch/accounts.html', context )

def mappings(request):
    return render(request, 'maps.html', context )

def validate_upi(request):
    upi = request.GET.get('id_uname')
    
    print(upi)
    data = {
        'is_taken': My_Students.objects.filter(ups_number=upi).exists()
    }

    print(data['is_taken'])
    return JsonResponse(data)
