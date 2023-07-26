from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:news_id>', views.news_details, name='news-details')
]
