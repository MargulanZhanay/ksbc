from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=128
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст вашего поста'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
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

    def __str__(self):
        return self.text[:15]
