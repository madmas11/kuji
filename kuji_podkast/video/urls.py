from django.urls import path
from . import views
# from .views import kuji_video, perst_video

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>', views.detail_video, name='detail'),
    # path('video/kuji_podkast/', kuji_video, name='podkast'),
    # path('video/perst_fomi/', perst_video, name='perst')
]
