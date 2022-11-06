from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def privacy(request):
    """
    A view to display Privacy Policy
    """
    return render(request, 'privacy/privacy.html')


def terms(request):
    """
    A view to display Terms and Conditions
    """
    return render(request, 'terms/terms.html')
