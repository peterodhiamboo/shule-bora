from django.shortcuts import render

# Create your views here.

def all_parents(request):
    context = {
        
    }
    return render(request, 'parents/index.html', context)
