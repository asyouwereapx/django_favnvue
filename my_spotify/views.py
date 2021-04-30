from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Spotify

def spotify_view(request):
	data = Spotify.objects.all()
	context = {"data": data}
	
	return render(request, "my_spotify/spotify_view.html", context)

def genre_view(request, genre):
	artists_by_genre = Spotify.objects.filter(genre = genre)
	# data = Spotify.objects.get(slug=slug)
	context = {
		'genre': genre,
		'artists_by_genre': artists_by_genre
	}
	
	return render(request, "my_spotify/genre_view.html", context)

def artist_view(request, artist):
	albums = Spotify.objects.filter(artist = artist)
	# data = Spotify.objects.get(slug=slug)
	context = {
		'artist': artist,
		'albums': albums
	}
	
	return render(request, "my_spotify/artist_view.html", context)

class GenresList(ListView):
	model = Spotify
	context_object_name = 'genres'
	template_name = 'my_spotify/genres_list.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		search = self.request.GET.get('search') or ''
		if search:
			context['genres'] = context['genres'].filter(genre__icontains=search)
		context['search_input'] = search
		return context

# class ArtistsList(ListView):
# 	model = Spotify
# 	context_object_name = 'artists'
# 	template_name = 'my_spotify/artists_list.html'


# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		search = self.request.GET.get('search') or ''
# 		if search:
# 			context['artists'] = context['artists'].filter(genre__icontains=search)
# 		context['search_input'] = search
# 		return context

# class AlbumsList(ListView):
# 	model = Spotify
# 	context_object_name = 'albums'
# 	template_name = 'my_spotify/albums_list.html'


# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		search = self.request.GET.get('search') or ''
# 		if search:
# 			context['albums'] = context['albums'].filter(genre__icontains=search)
# 		context['search_input'] = search
# 		return context

class SpotifyDetail(DetailView):
	model = Spotify
	# context_object_name = 'genre'

	template_name = 'my_spotify/artist_by_genre.html'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['artists'] = 
	# 	return context

	# data = Spotify.objects.filter(pk = kwargs['pk'])

	

