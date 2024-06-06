from django.contrib import admin
from .models import VideoYoutube, Channel


class VideoYoutubeAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id', 'description', 'published_at', 'parts', 'channel')
    search_fields = ('title', 'parts')
    list_filter = ('parts',)


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'channel_id')


admin.site.register(VideoYoutube, VideoYoutubeAdmin)
admin.site.register(Channel, ChannelAdmin)
