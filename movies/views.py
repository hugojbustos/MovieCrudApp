from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import Http404,request
from django.urls import reverse_lazy

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from . import mixins


class MovieListView(ListView):
    """Show all movies."""    
    model = Movie
    template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    """Show the requested movie."""
    model = Movie
    template_name = 'movies/movie_detail.html'


class MovieCreateView(mixins.SuccessMessageMixin,CreateView):
    """Create a new movie."""
    model = Movie
    fields ='__all__'
    template_name = 'movies/movie_form.html'
    success_url = '/movies/'
    success_message = 'The movie created successfully'
    error_message = 'The creation has failed'
    

class MovieUpdateView(mixins.SuccessMessageMixin,UpdateView):
    """Update the requested movie."""
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_form.html'
    success_message = 'The movie updated successfully'
    error_message = 'The update has failed'


class MovieDeleteView(mixins.SuccessMessageMixin,DeleteView):
    """Delete the requested movie."""
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_confirm_delete.html'
    success_url = '/movies/'
    success_message = 'The movie deleted successfully'
    error_message = 'The updated has failed'

class MovieListCreate(generics.ListCreateAPIView):
    """ Movies API """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieReviewCreate(generics.ListCreateAPIView):
    """ Movies Review API """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class ToplistListView(ListView):
    """ Movies ordered by rating desc """
    model = Movie
   # template_name = "movies/toplist.html"

    def get_queryset(self):
        return Movie.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')