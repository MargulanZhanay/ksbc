from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from .models import Events

EVENTS_PER_PAGE = 6
CACHE_SECONDS = 20


@cache_page(CACHE_SECONDS)
def past_events(request):
    events_list = Events.objects.order_by('-pub_date')
    paginator = Paginator(events_list, EVENTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'events/past-events.html', context)


@cache_page(CACHE_SECONDS)
def upcoming_events(request):
    events_list = Events.objects.order_by('-pub_date')
    paginator = Paginator(events_list, EVENTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'events/upcoming-events.html', context)


def events_details(request, events_id):
    event = get_object_or_404(Events, id=events_id)
    context = {
        'event': event
    }
    return render(request, 'events/event_details.html', context)
