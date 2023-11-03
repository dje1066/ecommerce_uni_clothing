from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Userprofile

# Create your views here.


def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            # once user is done signing up, they are redirected to the front page
            return redirect('frontpage')
    else:
        form = UserCreationForm()  # if user doesn't submit form

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
