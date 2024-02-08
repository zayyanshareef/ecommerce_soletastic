from django.urls import path
from . import views


urlpatterns = [
    path('',views.Admin,name="admin_login"),
    # path('admin_dashboard/',views.Admin_dashboard,name="admin_dashboard")

    
    
]