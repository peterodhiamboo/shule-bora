from django.shortcuts import render, redirect
from my_class.models import Class_Layout

# Create your views here.

def profile(request):
    my_classes = Class_Layout.objects.all().order_by('date_added')

    if request.user.is_authenticated:
        # Do something for authenticated users.
        context = {
        'classes': my_classes,
        }
        return render(request, 'user_profile/index.html', context)
    else:
        # Do something for anonymous users.
        return redirect('login')
