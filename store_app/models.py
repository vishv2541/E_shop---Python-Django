
#from collections import OrderedDict
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name

class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 to 2000','1000 to 2000'),
        ('1000 to 10000','10000 to 20000'),
        ('20000 to 30000','30000 to 40000'),
        ('40000 to 50000','50000 to 60000'),
    )           
    price = models.CharField(choices=FILTER_PRICE,max_length=100)

    
    def __str__(self):
        return self.price

class Product(models.Model):
    CONDITION = (('New','New'),('old','old'))
    STOCK = (('in stock','in stock'),('out of stock','out of stock'))
    STATUS = (('publish','publish'),('draft','draft'))

   # unique_id = models.CharField(unique=True,max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="myimage")
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=100)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK,max_length=100)
    status = models.CharField(choices=STATUS,max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    #def save(self,*args,**kwargs):
        #if self.unique_id is None and self.created_date and self.id:
           # self.unique_id = self.created_date.strftime('75%Y%m%d23')+str(self.id)
           # return super().save(*args,**kwargs)
        
        
    def __str__(self):
        return self.name
        

class Images(models.Model):
    image = models.ImageField(upload_to="myimage")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)    

class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class Order(models.Model):
    firstname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    order_id = models.CharField(max_length=100,null='True',default='')
    amount = models.CharField(max_length=100,null='True',default='')

    def __str__(self):
        return self.firstname
    
class orderitem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/myimage")
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=1000)

    def __str__(self):
        return self.order.firstname
    

