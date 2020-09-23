from rest_framework import serializers
from .models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'year','rated', 'released_on', 'genre', 'director', 
'plot')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('reviewed_film', 'comments','rating')


      