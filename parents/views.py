from django.shortcuts import render
from . models import Parents

# Create your views here.

def all_parents(request):
    parents = Parents.objects.all()
    context = {
        'parents':parents,
    }
    return render(request, 'parents/index.html', context)
