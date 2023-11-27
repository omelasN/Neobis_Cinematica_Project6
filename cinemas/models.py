from django.db import models
from movies.models import Movie
from users.models import User


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Seat(models.Model):
    row = models.IntegerField(default=1)
    number_of_seat = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.row} - {self.number_of_seat}"


class ShowTime(models.Model):
    show_time = models.TimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cinema} - {self.movie} | {self.show_time}"


class Discount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.BooleanField()

    def __str__(self):
        return self.discount


class Ticket(models.Model):
    PAYMENT = {
        ('card', 'картой'),
        ('cash', 'наличными')
    }
    payment = models.CharField(max_length=12, choices=PAYMENT)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    film_name = models.ForeignKey(Movie, related_name='related_film_name', on_delete=models.CASCADE)
    cinema_name = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    price = models.ForeignKey(Movie, related_name='related_price', on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.film_name} | {self.cinema_name}"
                f" {self.room_name} | {self.seat}"
                f" {self.show_time} | {self.price}"
                f"{self.quantity} | {self.total_amount}"
                f"{self.payment}")

