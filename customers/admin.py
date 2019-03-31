from django.contrib import admin
from movies.models import Movies
from customers.models import Customers

admin.site.register(Movies)
admin.site.register(Customers)
# Register your models here.
