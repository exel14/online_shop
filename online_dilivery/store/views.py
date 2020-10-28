from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm

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
    context = {'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'store/customer.html',context)

def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
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