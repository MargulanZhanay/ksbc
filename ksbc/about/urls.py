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
]
