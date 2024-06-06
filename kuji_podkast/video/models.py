from django.db import models


class Channel(models.Model):
    name = models.CharField('Название канала', max_length=250)
    channel_id = models.CharField('id канала', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class VideoYoutube(models.Model):
    SEGMENTS = {
        'kuji': 'Kuji-podcast',
        'perst': 'Perst fomi'
    }
    title = models.CharField('Заголовок', max_length=100)
    video_id = models.CharField('Сылка на видео', max_length=250)
    description = models.TextField('Описание', )
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    parts = models.CharField('Разделы', choices=SEGMENTS, max_length=100)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='Канал')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео-ролик'
        verbose_name_plural = 'Видео-ролики'
