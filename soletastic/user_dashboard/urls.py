from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Dashboard,name = 'dashboard'),
    path('all_product',views.All_product,name = 'all_product'),
    path('view_product/<int:id>',views.View_product,name ='view_product'),
    path('user_profile/',views.User_Profile,name='user_profile'),
    path('edit_profile/<int:id>',views.Edit_profile,name="edit_profile"),
    path('address/',views.Address,name="address"),
    path('add_address/',views.Add_address,name="add_address"),
    path('delete_address/<int:id>',views.Delete_address,name="delete_address"),
    path('edit_address/',views.Edit_address,name="edit_address"),
    path('cart/',views.User_cart,name="user_cart"),
    path('add-to-cart/',views.Add_to_cart,name="add_to_cart"),
    # path('delete_cart/<int:id>/', views.Delete_cart, name="delete_cart"),
   
    
]
