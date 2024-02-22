from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.cache import  never_cache,cache_control
from django.contrib.auth.decorators import login_required
from admin_app.models import *
from user_auth.models import *
from . models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
import re 
from django.http.response import JsonResponse


# Create your views here.



#//////////////////////////////////..Dashboard..//////////////////////////
@never_cache
@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def Dashboard(request):

  pro=Product.objects.all()
  for i in pro:
     print(pro)
  context={
    'pro':pro
  }
  return render(request,'user_dashboard/dashboard.html',context)



#///////////////////////////////..All product..//////////////

def All_product(request):
    
    pro=Product.objects.all()
    
    context={
        'pro' : pro
    }
    
    return render(request,'user_dashboard/all_product.html',context)



#/////////////////////////////////..view product../////////////

def View_product(request,id):
    
  try:
    
      pro=get_object_or_404(Product,id=id)
      out_of_stock=Product_size.objects.filter(stock__gte=1,product=id)

      if not out_of_stock:
         stock=False
      else:
         stock=True

      context={
        
          'pro' : pro,
          'stock':stock
       
      }
    
      return render(request,'user_dashboard/view_product.html',context)
  
  except TypeError:
     return render(request,"user_dashboard/error.html")
  





  #...................................user profile........................

@login_required(login_url='user_auth/login/')
@never_cache
def User_Profile(request):
     try:
     
        if request.user.is_authenticated:
       
           user_details = Custom_User.objects.get(email=request.user)
           
           context={
              'user' : user_details,
           }

           return render(request,'user_dashboard/profile.html')
    
        return redirect ("login")
     
     except TypeError:
        return  render(request,'user_dashboard/error.html')
     





def Edit_profile(request,id):


   try:
      if request.method=='POST':

         username =request.POST.get("editFirstName")
         email=request.POST.get("editEmail")
         phone=request.POST.get("editphone")
         print("ahaghfagha")


         pattern = r'^[a-zA-Z0-9].*'
         pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
         pattern_Phone= r'^(?!0{10}$)\d{10}$'

         if not (username or email or phone):
            messages.error(request,"please fill required field")
            return render(request,"user_dashboard/profile.html")
         

         if not re.match(pattern,username):
            messages.error(request,"please enter valid user name")
            return render(request,"user_dashboard/profile.html")
         
         elif not re.match(pattern_email,email):
            messages.error(request,"please enter valid email address")
            return render(request,"user_dashboard/profile.html")
         


         elif not re.match(pattern_Phone,phone):
            messages.errror(request,"please eneter valid phone number")
            return render(request,'user_dashboard/profile.html')
         
         Custom_User.objects.filter(id=id).update(username=username,email=email,ph_no=phone)

         return render(request,"user_dashboard/profile.html")
      

   except TypeError:
      return render(request,"user_dashboard/error.html")
  
  
  #.................................... Edit_profile.......................................
@login_required(login_url='/user_auth/Login/')
@never_cache
def Address(request):
      try:
         if request.user.is_authenticated:
            user=Custom_User.objects.get(email=request.user)
            value=User_Address.objects.filter(customuser=user.id)

            context={

               'value' :value
            }

            return render(request,'user_dashboard/address.html',context)
         return redirect('user_profile')
      except TypeError:
         return render(request,"user_dashboard/error.html")
      




#............................add address.................................
      

def Add_address(request):
   try:
      if request.user.is_authenticated:
         user=Custom_User.objects.get(email=request.user)

         if request.method == "POST":

            name=request.POST.get("name")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            house=request.POST.get("house")
            street=request.POST.get("street")
            city=request.POST.get("city")
            state=request.POST.get("state")
            country=request.POST.get("country")
            pin_code=request.POST.get("pin_code")
            location=request.POST.get("location")



            pattern = r'^[a-zA-Z0-9].*'
            pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            pattern_Phone= r'^(?!0{10}$)\d{10}$'


            if not (name or email or phone or house or street or city or country or pin_code or location):
                                messages.error(request, "please Fill Required Field")
                                return redirect("address")
                            
            if not all(re.match(pattern, value) and value.strip() for value in [name, email, phone, house, street, city,country, state, pin_code, location,]):
                                messages.error(request, "Please Enter Valid values")
                                return redirect("address")
                            
            elif not re.match(pattern_email,email):
                                messages.error(request,"Please enter valid email address")
                                return redirect("address")
                            
            elif not re.match(pattern_Phone,phone):
                                messages.error(request,"Please enter valid Phone number")
                                return redirect("address")
                            
                        
            value=Custom_User.objects.get(id=user.id)
                        
                        
            User_Address.objects.create(
                 
                            
               name=name,
               email=email,
               phone=phone,
               house=house,
               street=street,
               city=city,
               state=state,
               country=country,
               pin_code=pin_code,
               location=location,
               customuser= value,            
                                                    )
                
                
            return redirect("address")
                
                
         return redirect("address")
      return redirect("login")
        
   except TypeError:
        return render(request,'dashbord/error.html')
   

#...................................delete adddress......................
def Delete_address(request,id):
    
    try:
        
        if id:
           
           User_Address.objects.filter(id=id).delete()
           
           
           
           return redirect("address")
        
        return redirect("address")
        
        
    
    except TypeError:
        return render(request,'dashbord/error.html') 



#............................edit address..................

def Edit_address(request):

     try:
          if request.method == "POST":
               E_name=request.POST.get("editname")
               E_name=request.POST.get("editName")
               E_email=request.POST.get("editEmail")
               E_phone=request.POST.get("editphone")
               E_house=request.POST.get("editHouse")
               E_street=request.POST.get("editStreet")
               E_city=request.POST.get("editcity")
               E_state=request.POST.get("editstate")
               E_country=request.POST.get("editcountry")
               E_pin_code=request.POST.get("editpin_code")
               E_location=request.POST.get("editlocation")
               address_id = request.POST.get('editid')


               pattern = r'^[a-zA-Z0-9].*'
               pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
               pattern_Phone= r'^(?!0{10}$)\d{10}$'

               if not (E_name or E_email or E_phone or E_house or E_street or E_city or E_country or E_pin_code or E_location):
                        messages.error(request, "please Fill Required Field")
                        return redirect("address")
               
               if not all(re.match(pattern, value) and value.strip() for value in [E_name, E_house, E_street, E_city, E_country, E_pin_code, E_location]):
                        messages.error(request,"Please Enter Valid values")
                        return redirect("address")

               elif not re.match(pattern_email,E_email):
                        messages.error(request,"Please enter valid email address")
                        return redirect("address")
               
               elif not re.match(pattern_Phone,E_phone):
                        messages.error(request,"Please enter valid Phone number")
                        return redirect("address")
               
               User_Address.objects.filter(id=address_id).update(name=E_name,
                                                               email=E_email,
                                                               phone=E_phone,
                                                               house=E_house,
                                                               street=E_street,
                                                               city=E_city,
                                                               state=E_state,
                                                               country=E_country,
                                                               pin_code=E_pin_code,
                                                               location=E_location
                                                               )
               return redirect("address")
     except TypeError:
          return render(request,"user_dashboard/error.html")
     
#.......................user cart........................................
@login_required(login_url='user_auth/login/')
@never_cache
def User_cart(request):
     try:
          if request.user.is_authenticated:
               cart=Cart.objects.filter(customuser=request.user)

               sub=request.session.get("sub_total")

               if not sub:
                  sub_total=0
                  for i in cart:
                         
                     sub_total+=int(i.total_price)
                  request.session["sub_total"]=sub_total
                  sub=request.session.get("sub_total")
               else:
                  sub_total=0
                  for i in cart:
                         
                        sub_total +=int(i.total_price)
                  request.session["sub_total"]=sub_total
                  sub=request.session.get("sub_total")


               context={
                    
                    'cart':cart,
                    'sub_totel' : sub,
               }
               return render(request,'user_dashboard/cart.html',context)
          return redirect('login')
     except TypeError:
          return render(request,'user_dashboard/error.html')
                    
     





         
#.................................... ADD TO CART...............................
     
@login_required(login_url='/user_auth/Login/')
@never_cache
def Add_to_cart(request):
   try:
      print(",,,,,,,,,,,,,,,,,")
      if request.method == 'POST':
         if request.user.is_authenticated:
            pro_id=request.POST.get('product_id')
            pro_size=request.POST.get('product_size')
            product=Product.objects.get(id=pro_id)

            product_check=Product.objects.get(id=pro_id)
            print("//////////////////////////")

            if(pro_size):
              if(product_check):
                  if Cart.objects.filter(customuser=request.user,product=pro_id,size=pro_size).exists():
                     return  JsonResponse({'status':"product already in cart"})
                  else:
                    pro_qty=request.POST.get("product_qty")

                  
                        
                    total =int(product_check.price)* int(pro_qty)
                    


                    Cart.objects.create(customuser=request.user,
                                        product=product,
                                        size=pro_size,
                                        qty=pro_qty,
                                        price=int(product_check),
                                        total_price=total)
              else:
                 return JsonResponse({'status' :"No such product found"})
            else:
                    
              return JsonResponse({'status' :"Please select Your Size"})
                    
                            
      else:
                        
        messages.error(request,"Login to Continue")
        return redirect("login")
                
            
        
      return redirect("view_product")
   
   except TypeError:
        return render(request,'dashbord/error.html')
    
#......................................end add to cart..................................



#//////////////////////////////////   delete from cart ///////////////////////
# def Delete_cart(request,id):
    
#     try:
#         print(id)
#         value=Cart.objects.get(id=int(id))
        
        
#         if "sub_total" in request.session:
        
#             sub=request.session.get("sub_total")
            
#             sub_total=  int(sub) - int(value.total_price)
            
#             if "sub_total" in request.session:
#                 del request.session["sub_total"]
                

#             request.session["sub_total"]=sub_total
#             value.delete()
        
#         return redirect('user_cart')
    
#     except TypeError:
#         return render(request,'user_dashbord/error.html')
    
                    

                     



