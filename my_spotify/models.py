from django.db import models

class Spotify(models.Model):
	genre = models.SlugField(max_length=20, null = True, blank=True)
	artist = models.CharField(max_length=30, null = True, blank=True)
	album = models.CharField(max_length=20, null = True, blank=True)
	# slug = models.SlugField(max_length=30, null = True)

	# def __str__(self):
	# 	return self.artist

	class Meta:
		db_table = "spotify"
		ordering = ['genre']


