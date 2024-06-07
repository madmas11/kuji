from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/', views.user_page, name='user_page'),
    # path('<str:username>/', user_detail, name='user_detail'),
    # path('<str:username>/edit', UserUpdateView.as_view(), name='edit_user'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]