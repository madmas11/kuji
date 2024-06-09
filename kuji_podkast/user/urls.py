from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/', views.user_page, name='user_page'),
    path('<str:username>/profile/', views.user_profile, name='user_profile'),
    path('<str:username>/favorites/', views.user_favorites, name='user_favorites'),
    path('<str:username>/comments/', views.user_comments, name='user_comments'),
]