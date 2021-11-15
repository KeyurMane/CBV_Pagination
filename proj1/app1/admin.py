from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['ename','edept','esal']

admin.site.register(Employee,EmployeeAdmin)
