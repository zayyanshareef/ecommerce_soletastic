from django.db import models
from user_auth.models import *
from admin_app.models import *
# Create your models here.


class Cart(models.Model):
    customuser=models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(null=False,blank=False)
    size=models.IntegerField(null=False,blank=False)
    price=models.IntegerField(null=False,blank=False)
    
    total_price=models.IntegerField(null=False,blank=False)
