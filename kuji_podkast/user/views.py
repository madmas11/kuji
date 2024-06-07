from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
from .forms import CustomUserChangeForm


def user_page(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_page', username=user.username)
    else:
        form = CustomUserChangeForm(instance=user)

    title = f'Страница пользователя {user}'
    data = {'user_name': user,
            'title': title,
            'form': form}
    return render(request, 'user_page.html', data)
