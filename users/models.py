from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from movies.models import Movie


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = UserManager()
    REQUIRED_FIELDS = ['email']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def str(self):
        return f"{self.username}"


class Feedback(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about_film = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.about_film}"
