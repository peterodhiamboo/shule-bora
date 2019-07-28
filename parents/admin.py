from django.contrib import admin
from parents.models import Parents

# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    model = Parents
    list_display = ['full_name','phone_number','student']


admin.site.register(Parents, ParentAdmin)
