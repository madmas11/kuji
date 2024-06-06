from django.core.paginator import Paginator
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


def kuji_video(request):
    video_t = VideoYoutube.objects.filter(parts='kuji').order_by('-published_at')
    paginator = Paginator(video_t, 4)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    data = {'title': 'Kuji-подкаст',
            'video': page.object_list,
            'page': page
            }
    return render(request, 'video/kuji_podkast.html', data)


def perst_video(request):
    video_t = VideoYoutube.objects.filter(parts='perst').order_by('-published_at')
    paginator = Paginator(video_t, 4)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    data = {'title': 'Перст фомы',
            'video': page.object_list,
            'page': page}
    return render(request, 'video/perst_fomi.html', data)