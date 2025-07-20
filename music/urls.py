from django.urls import path
from . import views
from .views import upload_song,get_songs

urlpatterns = [
    path('', views.home, name='home'),
    path("upload/", upload_song, name="upload_song"),
      path('get_songs/', get_songs, name='get_songs'),
    
]
