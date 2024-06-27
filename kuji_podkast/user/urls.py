from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/', views.user_page, name='user_page'),
    path('<str:username>/profile/', views.user_profile, name='user_profile'),
    path('<str:username>/favorites/', views.user_favorites, name='user_favorites'),
    path('<str:username>/favorites/add/<int:video_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('<str:username>/favorites/remove/<int:video_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('<str:username>/comments/', views.user_comments, name='user_comments'),
    path('comments/delete/<int:comment_id>/', views.delete_comments, name='delete_comments'),
]