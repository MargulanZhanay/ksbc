from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('', views.AboutUsView.as_view(), name='index'),
    path('what-we-do/', views.WhatWeDoView.as_view(), name='what-we-do'),
    path(
        'our-structure/',
        views.OurStructureView.as_view(),
        name='our-structure'
    ),
    path('contact-us/', views.ContactUsView, name='contact-us'),

    path('mission/', views.MissionView.as_view(), name='mission'),
    path('vision/', views.VisionView.as_view(), name='vision'),

    path(
        'word-of-chairman/',
        views.WordOfChairmanView.as_view(),
        name='word-of-chairman'
        ),

    path(
        'board-of-directors/',
        views.BoardDirectorsView.as_view(),
        name='board-directors'
    ),
    path(
        'board-of-directors/sultan-marenov/',
        views.SultanView.as_view(),
        name='sultan-marenov'
    ),
    path(
        'board-of-directors/vincent-loh-weng-seng/',
        views.VincentView.as_view(),
        name='vincent-loh'
    ),
    path(
        'board-of-directors/eric-yew-tou-lim/',
        views.EricView.as_view(),
        name='eric-yew'
    ),
    path(
        'board-of-directors/olzhas-zhiyenkulov/',
        views.OlzhasView.as_view(),
        name='olzhas-zhiyenkulov'
    ),
    path(
        'board-of-directors/sean-soh-cheun-chong/',
        views.SeanView.as_view(),
        name='sean-soh'
    ),
    path(
        'board-of-directors/kenny-ng/',
        views.KennyView.as_view(),
        name='kenny-ng'
    ),
]
