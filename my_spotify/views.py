from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Spotify


class SpotifyList(ListView):
	model = Spotify
	context_object_name = 'genres'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		search = self.request.GET.get('search') or ''
		if search:
			context['genres'] = context['genres'].filter(title__icontains=search)
		context['search_input'] = search
		return context
	# template_name = 'my_spotify/genres'

class SpotifyDetail(DetailView):
	model = Spotify
	context_object_name = 'genre'
	template_name = 'my_spotify/artist_by_genre.html'

