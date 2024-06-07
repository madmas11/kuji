from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>', views.detail_video, name='detail'),
    path('kuji_podkast/', views.kuji_video, name='podkast'),
    path('perst_fomi/', views.perst_video, name='perst')
]
