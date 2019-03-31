from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from customers.forms import CustomerForm
from customers.models import Customers
from .forms import CustomerForm

from customers import urls
from django.conf.urls import url
@login_required(login_url='/accounts/login/')
def cust_add(request):
    if request.method == 'POST':
        form  = CustomerForm(request.POST)

        if form.is_valid():
            cust_name = form.cleaned_data['cust_name']
            cust_age = form.cleaned_data['cust_age']
            cust_address = form.cleaned_data['cust_address']
            cust_phone_number = form.cleaned_data['cust_phone_number']
            x = Customers(cust_name = cust_name,cust_age = cust_age,cust_address = cust_address,cust_phone_number = cust_phone_number)
            x.save()
            return redirect('cust_all')
    else:
        form = CustomerForm()
    return render(request,'customer_add.html',{'form':form})



@login_required(login_url='/accounts/login/')
def cust_all (request):

    allcustomers = {}
    customer1 = Customers.objects.all()
    allcustomers['customer_data'] = customer1
    print(allcustomers)
    return render(request, 'customer_all.html' ,allcustomers)


# def cust_update(request, id):
#     cust_upd = Customers.objects.get(id=id)
#     if request.method == 'POST':
#         form2 = forms.CustomerForm(request.POST,instance=cust_upd)
#         if form2.is_valid():
#             j = form2.save(commit = False)
#             j.save()
#             return redirect('cust_all')
#     else:
#         form2 = forms.CustomerForm(instance = cust_upd)
#     return render(request, 'customer_add.html', {'form': form2})
@login_required(login_url='/accounts/login/')
def cust_update(request,id):
    cust_updt=Customers.objects.get(id=id)

    if request.method == 'POST':
        form = forms.CustomerForm(request.POST,instance=cust_updt)
        if form.is_valid():
              z = form.save(commit = False )
              z.save()
              return redirect('cust_all')
    else :
            form = forms.CustomerForm(instance=cust_updt)
    return render(request,'customer_add.html',{'form': form})

# def cust_update(request, id):
#
# cust_upd = Customers.objects.get(id=id)
#     if request.method == 'POST':
#         form2 = forms.CustomerForm(request.POST,instance=cust_upd)
#         if form2.is_valid():
#             j = form2.save(commit = False)
#             j.save()
#             return redirect('cust_all')
#     else:
#         form2 = forms.CustomerForm(instance = cust_upd)
#     return render(request, 'customer_add.html', {'form': form2})
@login_required(login_url='/accounts/login/')
def cust_delete(request,id):
    y = Customers.objects.get(id=id)
    y.delete()
    return redirect('cust_all')



