from django import forms
from . import models

class MovieForm(forms.ModelForm):

    class Meta:
        model = models.Movies
        fields = ['movie_name','movie_genre','movie_language','movie_price','movie_year']





