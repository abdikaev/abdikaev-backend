from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=2000, default='')
    due_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(null=False, default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'ID: {self.id} {self.title}'


class BasketItem(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, default=1)

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'

    def __str__(self):
        return f'ID: {self.id} {self.owner} {self.movie.title} {self.amount}'
