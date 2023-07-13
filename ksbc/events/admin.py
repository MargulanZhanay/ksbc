from django.contrib import admin

# Register your models here.
from .models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'pub_date',
        'image',
        'url'
    )
    search_fields = ('title', )
    list_filter = ('pub_date', )

    empty_value_display = '-пусто-'


admin.site.register(Events, EventsAdmin)
