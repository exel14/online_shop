from django.shortcuts import render


def home_page(request):
    return render(request,'store/home.html')
def product_page(request):
    return render(request,'store/products.html')
def customer_page(request):
    return render(request,'store/customer.html')