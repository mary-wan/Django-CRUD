from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from.models import Employee
from django.urls import reverse


def add_employee(request):
    employees = Employee.objects.all()
    title ="ADD EMPLOYEE"
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("addEmployee"))
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html',{'employees':employees,'form':form,'title':title})

def update_employee(request,id):
    employees = Employee.objects.all()
    title ="UPDATE EMPLOYEE"
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("addEmployee"))

    else:
        form = EmployeeForm(instance = employee)

    return render(request, 'update_employee.html',{'form':form,'employees':employees,'title':title})

def delete_employee(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("addEmployee")  