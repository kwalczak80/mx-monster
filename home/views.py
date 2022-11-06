from django.shortcuts import render

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def privacy(request):
    """
    view to display Privacy Policy
    """
    return render(request, 'privacy_page/privacy.html')
