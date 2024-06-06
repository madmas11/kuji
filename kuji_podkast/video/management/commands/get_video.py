import os
from video.models import VideoYoutube, Channel
from googleapiclient.discovery import build
from django.core.management.base import BaseCommand

DEV_TOKEN = os.getenv('DEVELOPER_YOUTUBE_KEY')
channel_id = 'UCK8xpGAv8Oz7iMPgMw9j0LA'


class Command(BaseCommand):
    help = 'Команда по добавлению видео с ютуба'

    def handle(self, *args, **options):
        nextPageToken = None
        while True:
            youtube = build(
                'youtube',
                'v3',
                developerKey=DEV_TOKEN
            )
            request_video = youtube.search().list(
                part='snippet',
                channelId=channel_id,
                maxResults=50,
                order='date'
            )
            response = request_video.execute()
            videos_kuji = {}
            videos_perst = {}
            for item in response['items']:
                if item['id']['kind'] == 'youtube#video':
                    title = item['snippet']['title']
                    video_id = f'https://www.youtube.com/embed/{item["id"]["videoId"]}'
                    published_at = item['snippet']['publishedAt']
                    request_description = youtube.videos().list(
                        part='snippet',
                        id=item['id']['videoId']
                    )
                    response_description = request_description.execute()
                    for i in response_description['items']:
                        description = i['snippet']['description']
                        if 'Kuji Podcast' in title:
                            parts = 'kuji'
                            videos_kuji[title] = {
                                'video_id': video_id,
                                'published_at': published_at,
                                'description': description
                            }
                        elif 'Перст Фомы' in title:
                            parts = 'perst'
                            videos_perst[title] = {
                                'video_id': video_id,
                                'published_at': published_at,
                                'description': description
                            }
                    channel = Channel.objects.get(channel_id=channel_id)
                    VideoYoutube.objects.get_or_create(
                        title=title,
                        video_id=video_id,
                        published_at=published_at,
                        description=description,
                        parts=parts,
                        channel=channel
                    )
            nextPageToken = response.get('nextPageToken')

            if not nextPageToken:
                break