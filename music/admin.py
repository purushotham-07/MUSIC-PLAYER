
from django.contrib import admin
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("song_name", "singer", "movie", "language", "song_url", "image_url")
    search_fields = ("song_name", "singer", "movie", "language")
