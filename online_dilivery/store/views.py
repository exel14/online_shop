from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm
from .filters import OrderFilterSet
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'store/register.html',context)

def home_page(request):
    orders_count = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    not_delivered = Order.objects.filter(status='Not Delivered').count()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'customers':customers,'orders':orders,'orders_count':orders_count,
               'delivered':delivered,'pending':pending,'not_delivered':not_delivered}
    return render(request,'store/home.html',context)

def product_page(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/products.html',context)

def customer_page(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    filterset = OrderFilterSet(request.GET,queryset=orders)
    orders = filterset.qs #Обращаемся к классу Model
    context = {'customer':customer,'orders':orders,'orders_count':orders_count,
                   'filterset':filterset}
    return render(request,'store/customer.html',context)

def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderForm(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'customer':customer,'formset':formset}
    return render(request,'store/order_form.html',context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'store/order_form.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order':order}
    return render(request,'store/delete.html',context)