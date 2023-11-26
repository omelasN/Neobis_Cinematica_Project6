from django.db import models
from movies.models import Movie


class Cinemas(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=255)
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Seats(models.Model):
    row = models.IntegerField(default=1)
    number_of_seat = models.IntegerField(default=1)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.row} - {self.number_of_seat}"


class ShowTimes(models.Model):
    show_time = models.TimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cinema} - {self.movie} | {self.show_time}"
