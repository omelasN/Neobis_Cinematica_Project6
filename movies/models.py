from django.db import models


class MovieCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    status_choices = [
        ('ended', 'Ended'),
        ('ongoing', 'Ongoing'),
        ('soon', 'Soon')
    ]
    film_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.film_name

