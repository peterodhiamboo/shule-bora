from django.shortcuts import render
from my_class.models import Class_Layout

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
