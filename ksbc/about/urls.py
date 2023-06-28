from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('what-we-do/', views.WhatWeDoView.as_view(), name='what_we_do')
]
