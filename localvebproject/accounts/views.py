from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Currency, ExchangeRate, UserExchangeRate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')  # You
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def register_success(request):
    return render(request, 'accounts/register_success.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session["user_id"]=user.id
                    return render(request, 'accounts/profile.html', {'user': user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile(request):
    user=User.objects.get(id=request.session["user_id"])
    exchange_rates=UserExchangeRate.objects.filter(user=user).all()
    return render(request, 'accounts/profile.html',{'user': user,'exchange_rates':exchange_rates})

