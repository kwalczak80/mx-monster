""" Newsletter urls """
from django.urls import path
from . import views


urlpatterns = [
    path('newsletter_subscrition/',
         views.newsletter_subscribe,
         name='newsletter_subscribe'),
]