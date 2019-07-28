from django.shortcuts import render, redirect, HttpResponse
from my_class.models import Class_Layout
from students.models import My_Students, Fee
from django.http import JsonResponse
from django.contrib import messages, auth
from django.core.exceptions import ObjectDoesNotExist
from .alerts import Messages

my_classes = Class_Layout.objects.all().order_by('date_added')
student_count = My_Students.objects.count()

context = {
    'classes': my_classes,
    'student_count' : student_count,
}

def homepage(request):
    return render(request, 'goldentouch/index.html', context )

def accounts(request):
    return render(request, 'goldentouch/accounts.html', context )

def mappings(request):
    return render(request, 'maps.html', context )


def validate_upi(request): 
    if request.method == 'GET':
        upi = request.GET.get("upi")
        status = True

        try:
            stu = My_Students.objects.get(ups_number=upi)
        except ObjectDoesNotExist:
            status = False

        data = {
            'is_taken': status,
        }

        if status:
            name = stu.first_name
            fee = stu.school_fee()
            balance = Fee.compare(upi)

            print('Hello {}, your school fee is {} ,. but you have paid {}.'.format(name, fee, balance))

            # Compute whether fee paid is more than balance
            data = {
                'taken' : True,
            }
            
        else:
            data['msg'] = 'That is Invalid UPI'

        print(upi)
    return JsonResponse(data)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'admin/custom_login.html')


def validate_amount(request):
    if request.GET:
        amount = request.GET.get('amount')
        upi = request.GET.get('my_upi')

        data = dict()

        #Check whether object exists
        try:
            stu = My_Students.objects.get(ups_number=upi)
            name = stu.first_name
            fee = stu.school_fee()
            balance = Fee.compare(upi)

            total_difference = fee - balance
            # Make sure the amount paid is no greater than the balance owed

            if int(amount) > total_difference:
                data['taken'] = True
                print(amount)
                phrase_1 = 'Too much credit, you only have to pay {}'.format(total_difference)
                my_alert = Messages(phrase_1)
                data['balance_msg'] = my_alert.message['fee_error']
            else:
                data['taken'] = False
                my_alert = Messages('good amount !!')
                data['balance_msg'] = my_alert.message['fee_success']

        except ObjectDoesNotExist:
            data['taken'] = False
    elif request.POST: 
        upi = request.POST.get('upi')
        amount = request.POST.get('amount')
        remarks = request.POST.get('remarks')
        csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')

        #UPDATE STUDENT ACCOUNT WITH AMOUNT PAID
        payed_fee = Fee(student=upi, amount_paid=int(amount), remarks=remarks)
        payed_fee.save()

        response = {
            'name' : 'Success !!',
            'description' : 'Fee of KSH: {} deposited to UPI student account {}'.format(amount, upi),
            'version' : amount,
        }
        return JsonResponse(response)
    return JsonResponse(data)

