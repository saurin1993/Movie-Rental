from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import status
from customers.models import Customers
from . import forms
from movies.forms import MovieForm
from movies.models import Movies
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.serializers import MoviesSerializers

def movie_add(request):
    if request.method == 'POST':
        print(request.POST)
        form = MovieForm(request.POST)

        if form.is_valid():
            movie_name = form.cleaned_data['movie_name']
            movie_genre = form.cleaned_data['movie_genre']
            movie_language = form.cleaned_data['movie_language']
            movie_price = form.cleaned_data['movie_price']
            movie_year = form.cleaned_data['movie_year']

            m = Movies(movie_name=movie_name, movie_genre=movie_genre, movie_language=movie_language,
                       movie_price=movie_price, movie_year=movie_year)
            m.save()
            return redirect("movie_all")
    form = MovieForm()

    return render(request, 'movie_add.html', {'form': form})


def movie_delete(request, id):
        x = Movies.objects.get(id=id)
        x.delete()

        return redirect('movie_all')

def movie_all(request):
    allmovie = {}
    movie1 = Movies.objects.all()
    allmovie["movie_data"] = movie1
    return render(request, 'movie_all.html', allmovie)


def movie_available(request):
    m = {}
    movie1 = Movies.objects.filter(rentedBy=None)
    m["movie_data"] = movie1
    # return render(request, 'movie_available.html', m)
    return render(request, 'movie_available.html', m)


def movie_rented(request):
    m = {}
    movie1 = Movies.objects.exclude(rentedBy=None)

    m["movie_data"] = movie1

    return render(request, 'movie_rented.html', m)


def movie_update(request,id=id):
    movie_updt = Movies.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        form = forms.MovieForm(request.POST,instance=movie_updt)
        if form.is_valid():
            m=form.save()
            m.save()
            return redirect("movie_all")
    else:
        form = forms.MovieForm(instance=movie_updt)

    return render(request, 'movie_add.html', {'form': form})


class assignmovie(TemplateView):
    template_name = "movie_assign.html"

    # @method_decorator(login_required(login_url="homepage"))
    def get(self, request):
        movie = Movies.objects.filter(rentedBy__isnull=True)

        customer = Customers.objects.all()
        print(movie)
        print(customer)
        return render(request, "movie_assign.html", {"moviedata": movie, "customerdata": customer })

    def post(self, request):
        a = Movies.objects.get(id=request.POST["movie_id"])

        b = Customers.objects.get(id=request.POST["customer_id"])

        a.rentedBy = b
        print(a)
        a.save()

        return render(request, "movie_assign.html")





class MoviesViewset(APIView):

        def get(self,request,id=id):
            '''Get movie_object by id'''
            queryset = Movies.objects.get(id=id)
            serializer = MoviesSerializers(queryset)
            return Response(serializer.data)

        def delete(self,request,id=id):
            ''' delete Movie_object by id'''
            mov_delete = Movies.objects.get(id=id)
            mov_delete.delete()
            serializer = MoviesSerializers(mov_delete)
            return Response(status=status.HTTP_204_NO_CONTENT)



class Movies_data(APIView):

        def get(self,request):
            '''Gets all movie object'''
            movies = Movies.objects.all()
            serializer = MoviesSerializers(movies, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            '''Adds Movie object'''
            serializer = MoviesSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
















