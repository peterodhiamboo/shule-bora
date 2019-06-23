from django.shortcuts import render
from my_class.models import Class_Layout

# Create your views here.

def profile(request):
    my_classes = Class_Layout.objects.all().order_by('date_added')

    context = {
        'classes': my_classes,
    }
    return render(request, 'user_profile/index.html', context)
