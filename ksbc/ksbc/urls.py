from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('about.urls', namespace='about')),

    path('ksbcadminsecret/', admin.site.urls),
    path('news/', include('news.urls')),
    path('events/', include('events.urls'))

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
