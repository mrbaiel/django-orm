from django.shortcuts import render

from apps.hr.models import Employee


def homePageView(request):
    employees = Employee.objects.filter(about='Test')
    return render(request, 'list.html', {'employees': employees})

def empPageView(request):
    emp = Employee.objects.all()
    return render(request, 'emp_list.html', {'emps': emp})