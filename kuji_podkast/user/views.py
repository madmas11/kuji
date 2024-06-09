from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser, Favorite, Comment
from .forms import CustomUserChangeForm
from video.models import VideoYoutube


def user_page(request, username):
    user = get_object_or_404(CustomUser, username=username)
    title = f'Страница пользователя {user}'
    data = {
        'user': user,
        'title': title
    }
    return render(request, 'user_page.html', data)


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    title = f'Профиль {user}'
    saved = False
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = CustomUserChangeForm(instance=user)

    data = {'user_name': user,
            'title': title,
            'form': form,
            'saved': saved}
    return render(request, 'user_profile.html', data)


def user_favorites(request, username):
    user = get_object_or_404(CustomUser, username=username)
    title = f'Избранные видео {user}'
    favorites = Favorite.objects.filter(user=user).select_related('video')


    data = {
        'user': user,
        'title': title,
        'favorites': favorites
    }
    return render(request, 'user_favorites.html', data)


def user_comments(request, username):
    user = get_object_or_404(CustomUser, username=username)
    title = f'Комментарии {user}'
    comments = Comment.objects.filter(user=user).select_related('video')
    data = {
        'user': user,
        'title': title,
        'comments': comments,
    }
    return render(request, 'user_comments.html', data)