from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
import cloudinary.uploader
from .models import Song
from django.http import HttpResponse
from django.http import JsonResponse


from django.shortcuts import render
from .models import Song

def home(request):
    song = Song.objects.last() 
    if not song:
        return render(request, "main.html", {"song": None})  
    return render(request, "main.html", {"song": song})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url='/admin/login/')
def upload_song(request):
    if request.method == "POST":
        song_file = request.FILES.get("song_file")
        image_file = request.FILES.get("image_file")

        song_url = image_url = None  

        if song_file:
            song_upload = cloudinary.uploader.upload(song_file, resource_type="video")
            song_url = song_upload.get("secure_url")

        if image_file:
            image_upload = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = image_upload.get("secure_url")

        Song.objects.create(
            song_name=request.POST.get("song_name"),
            singer=request.POST.get("singer"),
            movie=request.POST.get("movie"),
            language=request.POST.get("language"),
            song_url=song_url,
            image_url=image_url
        )

        return render(request, "upload_success.html", {"song_url": song_url, "image_url": image_url})

    return render(request, "upload.html")

def music_player(request):
    songs = Song.objects.all() 
    return render(request, 'main.html', {'songs': songs})
from django.http import JsonResponse
from .models import Song 

from django.http import JsonResponse
from .models import Song  

def get_songs(request):
    language = request.GET.get('language', 'telugu').lower()  
    songs = Song.objects.filter(language__iexact=language)  

    if not songs.exists():
        return JsonResponse({"error": f"No songs found for language '{language}'"}, status=404)

    song_list = list(songs.values("song_name", "singer", "movie", "language", "song_url", "image_url"))
    
    return JsonResponse(song_list, safe=False)

