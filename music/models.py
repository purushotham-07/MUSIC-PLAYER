from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.models

class Song(models.Model):
    song_name = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    movie = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=50)
    song_url = models.URLField(blank=True, null=True)  
    image_url = models.URLField(blank=True, null=True)  

    def __str__(self):
        return f"{self.song_name} - {self.singer}"
