from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Dashboard,name = 'dashboard'),
    path('all_product',views.All_product,name = 'all_product'),
    path('view_product/<int:id>',views.View_product,name ='view_product'),
    
]
