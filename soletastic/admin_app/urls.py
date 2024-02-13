from django.urls import path
from . import views


#//////////////////////   Admin     ///////////////////////
urlpatterns = [
    path('',views.Admin,name="admin_login"),
    path('admin_dashboard/',views.Admin_dashboard, name="admin_dashboard"),
    path('admin_logout/',views.Admin_logout,name="admin_logout"),

    #/////////////////////  User list  /////////////////////
    

    path('user_list/',views.User_list,name="user_list"),
    path('user_unblock/<int:id>',views.User_unblock,name="user_unblock"),
    path('user_block/<int:id>',views.User_block,name="user_block"),
    

    #/////////////////////// category ////////////////////////////

    path('category_list/',views.Category_list,name="category_list"),
    path('add_category/',views.Add_category,name="add_category"),
    path('change_status/<int:id>',views.Change_status,name="change_status"),
    path('delete_category/<int:id>',views.Delete_category,name="delete_category"),
    path('update_category/<int:id>',views.Update_category,name="update_category"),


#////////////////////////////    sub category /////////////////////////

path('sub_category/',views.sub_category,name="sub_category"),
path('add_sub_category/',views.Add_sub_category,name="add_sub_category"),
path('status_change/<int:id>',views.Status_change,name="status_change"),
path('update_sub_category/<int:id>',views.Update_sub_category,name="update_sub_category"),
path('delete_sub_category/<int:id>',views.Delete_sub_category,name="delete_sub_category"),

#//////////////////////////////  product   ////////////////////////////

path('product_list/',views.Product_list,name="product_list"),
path('product_status/<int:id>',views.Product_status,name="product_status"),
path('add_product/',views.Add_product,name="add_Product"),
path('delete_product/<int:id>',views.Delete_product,name="delete_product"),
path('update_product/<int:id>',views.Update_product,name="update_product"),


#//////////////////////////////// size  /////////////////////////////////

path('add_size/<int:id>',views.Add_size,name="add_size"),
path('edit_size/<int:id>',views.Edit_size,name="edit_size"),

]