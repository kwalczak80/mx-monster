from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from profiles.models import UserProfile
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    Add a product review
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            Review.objects.create(user=user, product=get_object_or_404(Product,
                                  pk=product_id), description=description)
            messages.success(request, 'Thank you. Your review has been added successfully.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Please try again.')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
