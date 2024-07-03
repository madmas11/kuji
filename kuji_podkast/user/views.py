from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser, Favorite, Comment
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomUserAuthenticationForm

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
    title = f'Избранное видео {user}'
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


def add_to_favorites(request, username, video_id):
    user = get_object_or_404(CustomUser, username=username)
    video = get_object_or_404(VideoYoutube, id=video_id)

    Favorite.objects.get_or_create(user=user, video=video)

    return redirect('detail', pk=video_id)


def remove_from_favorites(request, username, video_id):
    user = get_object_or_404(CustomUser, username=username)
    video = get_object_or_404(VideoYoutube, id=video_id)

    favorite = Favorite.objects.filter(user=user, video=video)
    if favorite.exists():
        favorite.delete()

    return redirect('detail', pk=video_id)


def delete_comments(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('detail', pk=comment.video.id)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались.')
            return redirect('home')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f'{field.label}: {error}')
    else:
        form = CustomUserCreationForm()
    data = {
        'form': form,
        'title': 'Страница регистрации'
    }
    return render(request, 'register.html', data)



def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserAuthenticationForm()
    data = {
        'form': form,
        'title': 'Вход'
    }
    return render(request, 'login.html', data)


def logout_view(requset):
    logout(requset)
    return redirect('home')
