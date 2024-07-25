from django.shortcuts import render
from catalog.models import Product


def home(request):
    latest_products = Product.objects.order_by('-updated_at')[:5]
    for product in latest_products:
        print(product.name, product.price)
    return render(request, "home.html", {'latest_products': latest_products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, "contacts.html")
