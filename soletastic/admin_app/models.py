from django.db import models
from user_auth.models import *



# Create your models here.


class Category(models.Model):
    name=models.CharField( max_length=200)
    is_deleted=models.BooleanField(default=False)


class Sub_category(models.Model):

    name =models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    is_deleted=models.BooleanField(default=False)



class Product(models.Model):
    
    name=models.CharField(max_length=250)
    price=models.BigIntegerField()
    discount=models.DecimalField( max_digits=20, decimal_places= 2,null=True)
    sub_category=models.ForeignKey(Sub_category,on_delete=models.CASCADE) 
    description=models.TextField()
    is_deleted = models.BooleanField(default=False)
    image =  models.ImageField(upload_to='img/product')

    def __bool__(self):
        return  self.is_deleted
    
    def __iter__(self):
        
        return  self.id
    


class Product_size(models.Model):
    size=models.CharField(max_length=50,null=False)
    stock=models.IntegerField(null=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    

