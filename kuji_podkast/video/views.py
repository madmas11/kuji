from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import VideoYoutube
from user.models import Favorite, Comment
from user.forms import CommentForm
from .utils import pluralize_comments


def index(request):
    video_for_index = VideoYoutube.objects.order_by('-published_at')[:5]
    data = {
        'title': 'Kuji-подкаст на связи',
        'video_main': video_for_index
    }
    return render(request, 'index.html', data)


def detail_video(request, pk):
    video = VideoYoutube.objects.get(id=pk)
    user = request.user
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, video=video).exists()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.video = video
            comment.save()
            return redirect('detail', pk=video.id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(video=video).order_by('-post_date')
    count_comments = comments.count()
    comment_labels = pluralize_comments(count_comments)
    data = {
        'video': video,
        'is_favorite': is_favorite,
        'form': form,
        'comments': comments,
        'count_comments': count_comments,
        'comment_labels': comment_labels
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
