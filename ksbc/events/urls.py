from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('past-events/', views.past_events, name='past_events'),
    path('upcoming-events/', views.upcoming_events, name='upcoming_events')
]
