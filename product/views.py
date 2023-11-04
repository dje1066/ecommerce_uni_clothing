from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .cart import Cart

# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'product/cart_view.html', {
        'cart': cart
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # url representation
    return render(request, 'product/product_detail.html', {
        'product': product
    })
