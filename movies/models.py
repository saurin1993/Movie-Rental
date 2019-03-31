from django.db import models
from customers.models import Customers
genre=(("AC","Action"),("CM","Comedy"),("DR","Drama"),("HR","Horror"))
class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=2,choices=genre)
    movie_language = models.CharField(max_length=300)
    movie_price = models.IntegerField()
    movie_year = models.DateField(null=True,blank=True)
    rentedBy = models.ForeignKey('customers.Customers',on_delete=models.SET_NULL,null=True,blank=True)




    def __str__(self):
        return self.movie_name
# Create your models here.
