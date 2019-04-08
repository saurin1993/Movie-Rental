from movies.models import Movies
from rest_framework import serializers

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('movie_name','movie_genre','movie_language','movie_price','movie_year','rentedBy')