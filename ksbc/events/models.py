from datetime import date

from django.db import models


class Events(models.Model):
    title = models.CharField(
        verbose_name='Название мероприятия',
        max_length=250
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Описание вашему мероприятия'
    )
    pub_date = models.DateField(
        verbose_name='Дата события',
        db_index=True
    )
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='events/',
        blank=True
    )
    url = models.URLField(
        verbose_name='Ссылка регистрации',
        help_text='Ссылка регистрации на событие',
        max_length=255,
        blank=True
    )

    @property
    def date_overdue(self):
        return date.today() > self.pub_date

    @property
    def date_valid(self):
        return date.today() <= self.pub_date

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Событие',
        verbose_name_plural = 'События'

    def __str__(self) -> str:
        return self.text[:15]
