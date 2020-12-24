from django.db import models

# Create your models here.

#from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length = 50, null =  True)
    price = models.FloatField(null= True, blank = True )
   # catagory = models.CharField()
   # image = 

    def __str__(self):
       return self.product_name