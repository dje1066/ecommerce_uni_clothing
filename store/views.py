from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializer import ProductSerializer
from rest_framework import status

# Create your views here.

"""def index(request):
    categories = Category.objects.all()
    return render(request, 'frontpage.html', {'categories': categories})
"""

class FrontpageView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


def login(request):
    return render(request, 'userprofile/login.html')
