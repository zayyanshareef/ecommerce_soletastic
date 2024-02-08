from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # ................User Authentications.....................


    path('login/',views.Login,name ='login'),
    path('signup/',views.Signup,name="signup"),
    path('signupotp/',views.Signupotp,name='signupotp'),
    path('logout/',views.Logout,name='logout'),



    # .........................end..........................
]
