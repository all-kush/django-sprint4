from django.db import models

from .constants import MAX_LENGTH


class BaseModel(models.Model):
    """Абстрактная модель. created_at; флаг is_published"""

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')

    class Meta:
        abstract = True


class TitleModel(models.Model):
    """Абстрактная модель. Заголовок title"""

    title = models.CharField(max_length=MAX_LENGTH,
                             verbose_name='Заголовок')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
