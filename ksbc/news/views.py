from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News


NEWS_PER_PAGE = 6  # Number of news in a page.
CACHE_SECONDS = 20


def news(request):
    
    return render(request, 'news/news_list.html')
