from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView

class EmpListView(ListView):
    model = Employee
    template_name = 'emp_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'empl'  # Default: object_list
    paginate_by = 5
    queryset = Employee.objects.all()
