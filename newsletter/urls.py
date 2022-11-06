""" Newsletter urls """
from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('newsletter_subscrition/',
         views.newsletter_subscribe,
         name='newsletter_subscribe'),
]