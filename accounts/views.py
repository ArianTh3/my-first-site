from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomCreateUserForm, LoginForm
from django.contrib import messages
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "you Logged In successfully")
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "You have done something wrong. Please try again")
        form = LoginForm()
        context = {'form': form}    
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    
def register_view(request): 
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomCreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "you Signed up successfully")
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "You have done something wrong . Please try again")
        form = CustomCreateUserForm()
        return render(request, 'accounts/register.html', {"form":form})
    else:
        return redirect('/')
    