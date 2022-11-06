from django.shortcuts import render


def newsletter_subscribe(request):
    """
    A view to display the newsletter subscription page
    """
    return render(request, 'newsletter/newsletter_subscription.html')


def newsletter_signup(request):
    """
    A view to display the newsletter sign up page
    """
    return render(request, 'newsletter/newsletter_signup.html')
