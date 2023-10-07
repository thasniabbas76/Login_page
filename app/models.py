from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15) 
    description = models.TextField()
    def __str__(self) :
        return self.name
class Product(models.Model):
    item = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=500000)
    def __str__(self) :
        return self.item