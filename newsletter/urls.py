""" Newsletter urls """
from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('newsletter_subscrition/',
         views.newsletter_subscribe,
         name='newsletter_subscribe'),
    path('sign_up/', views.newsletter_signup,
         name='newsletter_signup'),
    path('unsubscribe/',
         views.newsletter_unsubscribe,
         name='newsletter_unsubscribe'),
]