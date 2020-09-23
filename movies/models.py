from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # Todo: add Rating models

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'pk': self.pk})


class Review(models.Model):
    reviewed_film = models.ForeignKey(Movie,related_name='reviews', on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )        

    def __str__(self):
        return self.reviewed_film.title