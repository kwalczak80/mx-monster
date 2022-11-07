from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ A view to display the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        sender = "Contact request from" + " " + str(email)
        msg_mail = str(message) + ", " + str(sender)
        if form.is_valid():
            send_mail(
                subject,
                msg_mail,
                email,
                [settings.DEFAULT_FROM_EMAIL, ]
            )
            form.save()
            messages.success(request, 'Thank you. Your Email has been sent !!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'An error occurred when trying to send your email message.\
                 Please check your form.'
            )
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
