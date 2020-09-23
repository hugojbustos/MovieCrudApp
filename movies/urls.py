from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', view=views.MovieListView.as_view(), name='index'),

    path('create/', view=views.MovieCreateView.as_view(), name='create'),

    path('toplist/', view=views.ToplistListView.as_view(), name='toplist'),

    path('<slug:pk>/',view=views.MovieDetailView.as_view(), name='detail'),   

    path('update/<slug:pk>/',view=views.MovieUpdateView.as_view(), name='update'),

    path('delete/<slug:pk>/',view=views.MovieDeleteView.as_view(), name='delete'),

    path('api/movie/', views.MovieListCreate.as_view() ),

    path('api/review/', views.MovieReviewCreate.as_view() ),
]
