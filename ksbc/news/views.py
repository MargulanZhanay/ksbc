from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from .models import News

NEWS_PER_PAGE = 9  # Number of news in a page.
CACHE_SECONDS = 20


@cache_page(CACHE_SECONDS)
def news(request):
    news_list = News.objects.order_by('-pub_date')
    paginator = Paginator(news_list, NEWS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'news/news_list.html', context)


def news_details(request, news_id):
    news = get_object_or_404(News, id=news_id)
    context = {
        'news': news
    }
    return render(request, 'news/news_details.html', context)
