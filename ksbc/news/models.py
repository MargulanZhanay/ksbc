from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField(
        max_length=128
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст вашего поста'
    )
    pub_date = models.DateField(
        verbose_name='Дата события',
        db_index=True
    )
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='news/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Новость',
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return self.text[:15]
