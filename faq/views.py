from django.shortcuts import render
from django.http import HttpResponse, request
from faq.models import Faq


def faq(request):
    """ Frequently asked questions """
    questions = Faq.objects.all().filter(is_published=True)
    context = {
        'questions': questions
    }
    return render(request, 'faq/faq.html', context)
