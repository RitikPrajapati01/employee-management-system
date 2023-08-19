from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeForm
from .models import Employees
from django.contrib import messages
# Create your views here.
def UserCreation(request):
    fm  = EmployeeForm
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = EmployeeForm()
    else:
        fm = EmployeeForm()
    user_data = Employees.objects.all() 

    if request.method == 'GET':
        nm = request.GET.get('my_names')
        if nm:
           your_data = Employees.objects.filter(id = nm)   
           return render(request, 'crud/home.html', {"forms":fm,'user_data':user_data,"your_data": your_data})              
        else:
            nm = 0    
            your_data = Employees.objects.filter(id = nm)  
            return render(request, 'crud/home.html', {"forms":fm,'user_data':user_data,"your_data": your_data})                      
    return render(request, 'crud/home.html', {"forms":fm,'user_data':user_data})              

def User_updation(request, id):
    if request.method == 'POST':
       pi = Employees.objects.get(pk = id)
       fm  = EmployeeForm(request.POST, instance=pi)
       if fm.is_valid():
          fm.save()
          messages.success(request,'Your Data Updated Successfully !!!')

    else:
        pi = Employees.objects.get(pk = id)
        fm = EmployeeForm(instance = pi)
    return render(request, 'crud/user_update.html', {'forms':fm})


def user_delete(request,id):
    user_info  =  Employees.objects.get(pk = id)
    user_info.delete()
    return HttpResponseRedirect('/')


def search(request):
    if request.method == 'GET':
        nm = request.GET.get('my_names')
        if nm:
            your_data = Employees.objects.filter(id = nm)
        else:
            nm = 0  
            your_data = Employees.objects.filter(id = nm)  
        return render(request, 'crud/home.html', {'your_data':your_data})
    return HttpResponseRedirect('/')    