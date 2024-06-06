from django.core.management.base import BaseCommand
from django.db.models import Count
from video.models import VideoYoutube


class Command(BaseCommand):
    help = 'Команда по удалению дубликатов из базы'

    def handle(self, *args, **options):
        duplicates = VideoYoutube.objects.values('title') \
            .annotate(title_count=Count('title')) \
            .filter(title_count__gt=1)

        for duplicate in duplicates:
            videos = VideoYoutube.objects.filter(title=duplicate['title'])[1:]
            video_ids = videos.values_list('id', flat=True)
            VideoYoutube.objects.filter(id__in=video_ids).delete()