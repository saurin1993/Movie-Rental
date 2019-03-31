from django.db import models

class Customers(models.Model):
    cust_name = models.CharField(max_length=100)
    cust_age = models.IntegerField()
    cust_address = models.CharField(max_length=200)
    cust_phone_number = models.IntegerField()
    cust_delete = models.CharField(max_length=100,null=True)
    cust_update = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.cust_name
