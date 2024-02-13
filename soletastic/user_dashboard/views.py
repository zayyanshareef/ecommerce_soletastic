from django.shortcuts import render,HttpResponse
from django.views.decorators.cache import  never_cache,cache_control
from django.contrib.auth.decorators import login_required
from admin_app.models import *
from user_auth.models import *
from . models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
import re 

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
    
      relate=Product.objects.exclude(id=id)[:4]
    
      context={
        
          'pro' : pro,
          'relate' : relate,
       
      }
    
      return render(request,'user_dashboard/view_product.html',context)
  
  except TypeError:
     return render(request,"user_dashboard/error.html")







