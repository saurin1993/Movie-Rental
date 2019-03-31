
from django.urls import path
from customers import views

urlpatterns = [

    path('add/',views.cust_add,name="cust_add"),
    path('all/',views.cust_all,name='cust_all'),
    path('update/<id>/',views.cust_update,name='cust_update'),
    path('delete/<id>/',views.cust_delete,name='cust_delete')

]
