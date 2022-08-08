from django.shortcuts import render, redirect
from . forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    obj = Employee.objects.all()
    context = {
        'obj':obj
    }
    return render(request,'employee_register/employee_list.html',context)

def employee_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            obj = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=obj)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            obj = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('/employee/list/')




def employee_delete(request,id):
    obj = Employee.objects.get(pk=id)
    obj.delete()
    return redirect('/employee/list/')