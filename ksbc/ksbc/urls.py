from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView)

urlpatterns = [
    path('', include('about.urls', namespace='about')),

    path('ksbcadminsecret/', admin.site.urls),
    path('news/', include('news.urls')),
    path('events/', include('events.urls')),
    path('', include('users.urls')),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path('', include('membership.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
