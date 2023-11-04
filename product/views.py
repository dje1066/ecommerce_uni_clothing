from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .cart import Cart

# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('frontpage')


def product_detail(request, slug):
    cart = Cart(request)
    print(cart.get_total_cost())

    product = get_object_or_404(Product, slug=slug)  # url representation
    return render(request, 'product/product_detail.html', {
        'product': product
    })
