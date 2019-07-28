from django.contrib import admin
from . models import My_Students, Fee

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    model = My_Students
    list_display = ['sur_name','first_name','last_name','student_class']

class FeeAdmin(admin.ModelAdmin):
    model = Fee
    list_display = ['student', 'amount_paid', 'paid_on']


admin.site.register(My_Students, StudentAdmin)
admin.site.register(Fee, FeeAdmin)
