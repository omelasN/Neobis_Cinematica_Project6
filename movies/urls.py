from django.urls import path
from .views import MovieViewSet, MovieCategoryViewSet, MovieUserView, MovieCategoryUserView


urlpatterns = [
    path('movie-admin/', MovieViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('movie_category-admin/', MovieCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('movie/', MovieUserView.as_view(), name="movie"),
    path('movie_category/', MovieCategoryUserView.as_view(), name="movie_category"),
]