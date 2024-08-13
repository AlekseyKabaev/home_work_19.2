from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactPageView(TemplateView):
    template_name = "contacts.html"

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')
        return render(request, "contacts.html")

# def products_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'products_list.html', context)


# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)

# def home(request):
#     latest_products = Product.objects.order_by('-updated_at')[:5]
#     for product in latest_products:
#         print(product.name, product.price)
#     return render(request, "home.html", {'latest_products': latest_products})
#
#

