
from django.urls import path
from movies import views
from movies.views import assignmovie

urlpatterns = [

    path('add/',views.movie_add,name="movie_add"),
    path('assign/',assignmovie.as_view(),name='movie_assign'),
    path('all/',views.movie_all,name='movie_all'),
    path('available/',views.movie_available,name='movie_available'),
    path('rented/',views.movie_rented,name='movie_rented'),
    path('update/<id>/',views.movie_update,name='movie_update'),
    path('delete/<id>/',views.movie_delete,name='movie_delete')



]
