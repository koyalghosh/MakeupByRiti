from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', views.index,name='admin'),
    path('',views.index,name='home'),
    path('contacts/',views.contacts,name='contacts'),
    path('about/',views.about,name='about')
]