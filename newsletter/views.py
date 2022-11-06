from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


def newsletter_subscribe(request):
    """
    A view to display the newsletter subscription page
    """
    return render(request, 'newsletter/newsletter_subscription.html')


def newsletter_signup(request):
    """
    A view to display the newsletter sign up page
    """
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             'Sorry, you have already subscribed to our newsletter!')
        else:
            messages.success(request,
                             'Congratulations !! You have successfully subscribed to our  newsletter!')
            instance.save()
            subject = "Thank you for Joining our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """Welcome to MX Monster Newsletter, \
                If you would like to unsubscribe visit \
                    https://mx-monster.herokuapp.com/newsletter/unsubscribe/"""
            send_mail(subject=subject,
                      from_email=from_email,
                      recipient_list=to_email,
                      message=signup_message,
                      fail_silently=False)

    context = {
        'form': form,
    }

    template = 'newsletter/newsletter_signup.html'

    return render(request, template, context)


def newsletter_unsubscribe(request):
    """ Newsletter unsubscribe """
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                             'Your email has been \
                                 deleted from our database.')
        else:
            messages.warning(request,
                             'Sorry but the email you provided \
                                 does not exist in our database!')

    context = {
        'form': form,
    }

    template = 'newsletter/newsletter_unsubscribe.html'

    return render(request, template, context)
