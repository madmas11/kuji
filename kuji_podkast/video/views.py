from django.shortcuts import render
from .models import VideoYoutube


def index(request):
    video_for_index = VideoYoutube.objects.order_by('-published_at')[:5]
    data = {
        'title': 'Kuji-подкаст на связи',
        'video_main': video_for_index
    }
    return render(request, 'index.html', data)


def detail_video(request, pk):
    video = VideoYoutube.objects.get(id=pk)
    data = {
        'video': video
    }
    return render(request, 'video/detail_video.html', data)
