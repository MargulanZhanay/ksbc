from django.core.paginator import Paginator
from django.shortcuts import render

from .models import News

NEWS_PER_PAGE = 6  # Number of news in a page.
CACHE_SECONDS = 20


def news(request):
    news_list = News.objects.order_by('-pub_date')
    paginator = Paginator(news_list, NEWS_PER_PAGE)
    page_number = request.POST.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'news/news_list.html', context)
