from django.urls import path
from .views import SpotifyList, SpotifyDetail


urlpatterns = [
    path('', SpotifyList.as_view(), name='index'),
    path('<int:pk>/', SpotifyDetail.as_view(), name='genre'),
]
