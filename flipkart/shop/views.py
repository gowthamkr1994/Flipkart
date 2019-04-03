from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from .models import Product,datetime

context={}
def home(request):
    p=Product.objects.all()
    # response = requests.get('http://dummy.restapiexample.com/api/v1/employees')
    # geodata = response.json()
    # return render(request, 'core/home.html',
    # context={'product':p,'ip': geodata[0]}
    # print("hello",geodata[0])
    cart=[]
    context = {'product': p,'cart':cart}
    return render(request,'shop/home.html',context)

def contact(request):
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def cart(request):
    return render(request,'shop/cart.html')

def profile(request):
    return render(request,'shop/profile.html')

