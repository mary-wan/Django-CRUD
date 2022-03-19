from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from.models import Employee
from django.urls import reverse


def add_employee(request):
    employees = Employee.objects.all()
    title ="ADD Employee"
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addEmployee')

    else:
        form = EmployeeForm()



    return render(request, 'addEmployee.html',{'employees':employees,'form':form,'title':title})
