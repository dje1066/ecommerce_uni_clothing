from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

# Create your views here.

"""def index(request):
    categories = Category.objects.all()
    return render(request, 'frontpage.html', {'categories': categories})
"""


def frontpage(request):
    products = Product.objects.all()  # get first 6 products on frontpage
    return render(request, 'store/frontpage.html', {
        'products': products
        # now can be used in template (.html)
    })


def cart(request):
    return render(request, 'product/cart_view.html')


def about(request):
    return render(request, 'store/about.html')


def signup(request):
    return render(request, 'userprofile/signup.html')
