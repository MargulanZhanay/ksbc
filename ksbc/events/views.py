from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Events

EVENTS_PER_PAGE = 6
CACHE_SECONDS = 20


def past_events(request):
    events_list = Events.objects.order_by('-pub_date')
    paginator = Paginator(events_list, EVENTS_PER_PAGE)
    page_number = request.POST.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'events/past-events.html', context)


def upcoming_events(request):
    events_list = Events.objects.order_by('-pub_date')
    paginator = Paginator(events_list, EVENTS_PER_PAGE)
    page_number = request.POST.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'events/upcoming-events.html', context)
