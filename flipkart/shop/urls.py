from django.contrib import admin
from django.urls import path
from . import views as shop_views

urlpatterns = [
    path('',shop_views.home,name="home"),
    path('contact/',shop_views.contact,name='contact'),
    path('about/',shop_views.about,name='about'),
    path('cart/',shop_views.cart,name='cart'),
    path('profile/',shop_views.profile,name='profile')
]
