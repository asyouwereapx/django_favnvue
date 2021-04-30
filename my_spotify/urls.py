from django.urls import path
from .views import GenresList, genre_view, artist_view


urlpatterns = [
    path('', GenresList.as_view(), name='genres'),
    # path('artist/', ArtistList.as_view(), name='artists'),
    # path('albums/', AlbumList.as_view(), name='albums'),
    path('<str:genre>/', genre_view, name = "genre"),
    path('albums/<str:artist>/', artist_view, name='artist'),
    # path('<int:pk>/', SpotifyDetail.as_view(), name='_genre'),
]
