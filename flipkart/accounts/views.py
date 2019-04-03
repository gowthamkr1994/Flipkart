from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from .forms import RegistrationForm
# from flipkart.shop import views as shop_views
context={}
# Create your views here.
# if request.session.has_key("user"):
#     userid = request.session["user"]


def index(request):
    return redirect('home')
     # return redirect('http://127.0.0.1:8000/')
    # return shop_views.home(request)

def register_view(request):
    if(request.method=='POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request, 'registration/register.html',context)

def login_view(request):
    if(request.method=='POST'):
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('valid user')
            user=form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form=AuthenticationForm()
    context={'form':form}
    return render(request,'registration/login.html',context)

def logout_view(request):
    print('reached logout')
    logout(request)
    return redirect('index')