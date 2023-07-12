from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'pub_date',
    )
    search_fields = ('title', )
    list_filter = ('pub_date', )

    empty_value_display = '-пусто-'


admin.site.register(News, NewsAdmin)
