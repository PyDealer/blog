from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published и дату поста"""
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True
