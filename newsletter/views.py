def newsletter_subscribe(request):
    """
    A view to display newsletter
	subscription page
    """
    return render(request, 'newsletter/newsletter_subscription.html')
