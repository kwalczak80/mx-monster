from django.shortcuts import render


def add_review(request):
    """
    A view to display the newsletter subscription page
    """
    return render(request, 'reviews/add_review.html')
