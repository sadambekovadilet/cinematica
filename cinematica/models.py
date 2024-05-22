from django.db import models


from common.models import nb, ABSModel
from account.models import User



class Janr(models.Model, ABSModel):
    name = models.CharField()


class Author(models.Model, ABSModel):
    first_name = models.CharField()
    last_name = models.CharField()
    middle_name = models.CharField(**nb)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}{" " + self.middle_name if self.middle_name else ""}'


class Movie(models.Model, ABSModel):
    name = models.CharField('Название фильма', db_index=True)
    janr = models.ForeignKey(Janr, models.CASCADE, related_name='movies')
    description = models.TextField()
    authors = models.ManyToManyField(Author)
    avatar = models.ImageField(upload_to='media/avatars')
    movie_file = models.FileField(upload_to='media/movies')
    main_artists = models.TextField()
    artists = models.TextField()


class ReviewToMovie(models.Model, ABSModel):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    STAR_CHOICES = (
        (ONE, 'ONE'),
        (TWO, 'TWO'),
        (THREE, 'THREE'),
        (FOUR, 'FOUR'),
        (FIVE, 'FIVE'),
    )

    stars = models.IntegerField(choices=STAR_CHOICES, **nb)
    review = models.TextField(**nb)
    movie = models.ForeignKey(Movie, models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, models.SET_NULL, related_name='reviews', **nb)

    class Meta:
        unique_together = [['user_id', 'movie_id']]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'