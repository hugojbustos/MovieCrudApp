from django.test import TestCase

from movies.models import Movie

print('prueba Get ',Movie.objects.get(pk=1))
movie = Movie.objects.get(pk=1)
print('prueba Get Url ',movie.get_absolute_url())
class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie.objects.get(pk=1)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.movie.get_absolute_url(),
            '/movies/1/'
        )

    def test_title(self):
        self.assertEqual(self.movie.title, 'Guardians of the Galaxy Vol. 2')
