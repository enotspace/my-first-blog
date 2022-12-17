import datetime
from django.db import models
from django.utils import timezone

class Game(models.Model):
    game_title = models.CharField('Назва гри', max_length=100)
    game_code = models.TextField('Код гри тре вставити в IDE')
    game_description = models.TextField('Опис гри')
    pub_date = models.DateTimeField('Дата публікації на сайті')

    def __str__(self):
        return self.game_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Гра'
        verbose_name_plural = 'Ігри'

class Comment(models.Model):
    gameapp = models.ForeignKey(Game, on_delete = models.CASCADE)
    author_name = models.CharField("Ім'я автора" , max_length=50)
    comment_text = models.TextField('Текст коментаря')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'