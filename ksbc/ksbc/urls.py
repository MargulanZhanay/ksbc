from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('about.urls', namespace='about')),

    path('ksbcadminsecret/', admin.site.urls),
    path('news/', include('news.urls')),
    path('events/', include('events.urls')),
    path('auth/', include('users.urls'))

]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
