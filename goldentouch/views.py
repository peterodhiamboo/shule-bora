from django.shortcuts import render


def homepage(request):
    return render(request, 'goldentouch/index.html', {})

def accounts(request):
    return render(request, 'goldentouch/accounts.html', {})
