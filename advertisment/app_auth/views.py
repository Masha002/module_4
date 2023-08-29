from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserCreationForm
from django.contrib.auth.models import User


def login_view(request):
    redirect_url = reverse('main_page')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html')

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            url = reverse('login')
            return redirect(url)
    else:        
        form = NewUserCreationForm()
    context = {'form' : form}
    return render(request, 'app_auth/register.html', context)