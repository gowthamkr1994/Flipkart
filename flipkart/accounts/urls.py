from django.contrib import admin
from django.urls import path
from . import views as acc_views
urlpatterns = [
        path(r'',acc_views.index,name='index'),
        path(r'register/',acc_views.register_view,name='register'),
        path(r'login/',acc_views.login_view,name='login'),
        path(r'logout/',acc_views.logout_view,name='logout')
]
