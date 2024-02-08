from django.shortcuts import render,HttpResponse

# Create your views here.


def Dashboard(request):
  
  return render(request,'user_dashboard/dashboard.html')