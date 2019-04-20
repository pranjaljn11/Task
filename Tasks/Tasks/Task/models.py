from django.db import models

#model TestObject for long running task
class TestObject(models.Model):
    name = models.CharField(max_length=30)
    phone =models.IntegerField()

#customer model with fields
class Customer(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Phone = models.IntegerField()

    def __str__(self):
        return self.First_Name

#Address model with fields for customer
class Address(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE) #for allowing multiple address of customer
    Address_Line = models.CharField(max_length=50)
    Locality = models.CharField(max_length= 50)
    City = models.CharField(max_length=20)

    def __str__(self):
        return self.City
