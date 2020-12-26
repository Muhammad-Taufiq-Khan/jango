from django.db import models

class Product(models.Model):

    
    CATAGORY = models.TextChoices('CATAGORY','Men Women Kid Other')
    product_name = models.CharField(max_length = 50, null =True)
    price = models.FloatField()
    image = models.ImageField(null = True, blank = True)
    catagory = models.CharField(blank = True, choices = CATAGORY.choices, max_length = 10 )
    
    @property
    def imageURL (self):
        try:
            url = self.image.url
        
        except:
            url = ''
        return url

    def __str__(self):
        return self.product_name
  