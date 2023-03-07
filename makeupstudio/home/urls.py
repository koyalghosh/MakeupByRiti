from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', views.index,name='about'),
    path('',views.index,name='home')
]