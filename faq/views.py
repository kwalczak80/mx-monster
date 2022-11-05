from django.shortcuts import render
from django.http import HttpResponse, request


def faq(request):
    """ Frequently asked questions """
    return render(request, 'faq/faq.html')
