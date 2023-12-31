# Generated by Django 4.2.7 on 2023-11-27 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_alter_movie_price"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cinemas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShowTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("show_time", models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name="Cinemas",
            new_name="Cinema",
        ),
        migrations.RenameModel(
            old_name="Rooms",
            new_name="Room",
        ),
        migrations.RenameModel(
            old_name="Seats",
            new_name="Seat",
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment",
                    models.CharField(
                        choices=[("cash", "наличными"), ("card", "картой")],
                        max_length=12,
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "total_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "cinema_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cinemas.cinema"
                    ),
                ),
                (
                    "film_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_film_name",
                        to="movies.movie",
                    ),
                ),
                (
                    "price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_price",
                        to="movies.movie",
                    ),
                ),
                (
                    "room_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cinemas.room"
                    ),
                ),
                (
                    "seat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cinemas.seat"
                    ),
                ),
                (
                    "show_time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cinemas.showtime",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="showtime",
            name="cinema",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cinemas.cinema"
            ),
        ),
        migrations.AddField(
            model_name="showtime",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
            ),
        ),
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("discount", models.BooleanField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
