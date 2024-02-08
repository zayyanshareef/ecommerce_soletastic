from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib import auth
import re
from .models import *
import random
from django.contrib.auth.hashers import make_password, check_password
from twilio.rest import Client
import os
from dotenv import load_dotenv
from django.contrib.auth.hashers import check_password
from django.views.decorators.cache import  never_cache,cache_control
from user_auth.models import Custom_User
from django.http import HttpResponse


# Create your views here.

@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    
    if  "user_email" in request.session :
        return render(request,'user_dashboard/dashboard.html')
    

    print("In")
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        User=authenticate(request, username=email, password=password)
   
        
        # try :
            
        #    status=Custom_User.objects.get(email=email)
        
        # except Exception as e:
            
        #     messages.error(request, "Email or Passwors mismatch")
        #     return render(request,'user_auth/Login.html')
        
        # if not status.is_active:
            
        #     messages.error(request, "Your account is Blocked")
        #     return render(request,'user_auth/Login.html')
        
        if User is not None  and not User.is_staff:
            request.session['user_email']=email
            login(request,User)
            return redirect('dashboard')
            
        else: 
            messages.error(request, "Email or Password mismatch")
            return render(request,'user_auth/Login.html')
            

    return render(request,'user_auth/Login.html')


@never_cache    
def Signup(request):

    if  "user_email" in request.session :
        return render(request,'user_dashboard/dashboard.html')


    if request.method == "POST":
        username = request.POST.get('username')
        lastname = request.POST.get('Lastname')
        email = request.POST.get('email')
        phone = request.POST.get('PhoneNumber')
        password = request.POST.get('password')
        confirmpass = request.POST.get("con_pass")

        # ............ REGEX PATTERN...............

        pattern= re.compile(r'^[a-zA-Z].*$')
        pattern_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pattern_Phone= re.compile(r'^(?!0{10}$)\d{10}$')
        pattern_pass = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')


        if not ( username and lastname and email and phone and password and confirmpass):
            messages.error(request,'Please fill required fields')
            return redirect('signup')
        
        elif not pattern.match(username and lastname):
            messages.error(request,'Please enter valid inputs')
            return redirect('signup')
            
        elif not re.match(pattern_email,email):
            messages.error(request,"Please enter valid email")
            return redirect('signup')

        elif Custom_User.objects.filter(email = email).exists():
            messages.error(request,'email id already exists')
            return  redirect('signup') 
        
        elif not re.match(pattern_Phone,phone):
            messages.error(request,"Please enter valid Phone number")
            return redirect('signup')
        
        elif Custom_User.objects.filter(ph_no = phone).exists():
            messages.error(request,'Phone number already exists')
            return redirect('signup')
        
        elif not re.match(pattern_pass,password):
            messages.error(request,"The password is too weak")
            return redirect('signup')
        
        elif password != confirmpass:
            messages.error(request, 'Password and Confirm Password do not match')
            return redirect('signup')
        
        else:
            try:
                 values=otp()

            except Exception as e:
                 
                 messages.error(request,"OTP genaration failed")

        
        user_data = Custom_User.objects.create_user(email=email,password=password,username=username,ph_no=phone)
        user_data.save()
        
        
        request.session['otp']=values
        request.session['phone']=phone
        

        return redirect('signupotp')
    
    


        
    return render(request,'user_auth/signup.html')

# .................................OTP generation..................................


def otp():
            otp = random.randint(100000,999999)
            load_dotenv()
            my_number = os.getenv("MY_NUMBER")
            account_sid = os.getenv("TWILIO_ACCOUNT_SID")
            auth_token = os.getenv("TWILIO_AUTH_TOKEN")
            client = Client(account_sid,auth_token)

            msg = client.messages.create(
                body =F"Your OTP is {otp}",from_=+16502972288,to =my_number,
            )
            return otp


@never_cache
def Signupotp(request):
     
     if  "user_email" in request.session :
        return render(request,'user_dashboard/dashboard.html')
     

     otp=request.session.get("otp")

     print(otp,"otp")

     user = Custom_User.objects.get(ph_no =request.session.get('phone'))
     if request.method == "POST":
          action = request.POST.get('action')

          

          if action =='Verify':
               s_otp = request.POST.get("otp")
         
               if str(otp) == s_otp :
                    return redirect('login')
               else:
                    
                    messages.error(request,"otp mismatch")
                    return render(request,'user_auth/signup_otp.html')
               
          elif action =='cancel':
               user.delete()
               return redirect('signup')
          
          

     return render(request,'user_auth/signup_otp.html')

@never_cache
def Logout(request):
     
  
     if 'user_email' in request.session:
       
          logout(request)
          del request.session
          return render(request,'user_dashboard/dashboard.html')
     else:
  
        logout(request)

        return render(request,'user_dashboard/dashboard.html')
     