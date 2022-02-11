from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from student import views

app_name = 'student'

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),  
    
]
