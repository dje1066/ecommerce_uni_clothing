from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""def index(request):
    categories = Category.objects.all()
    return render(request, 'frontpage.html', {'categories': categories})
"""
def frontpage(request):
    return render(request, 'store/frontpage.html')

def about(request):
    return render(request, 'store/about.html')