""" Newsletter form """
from django import forms
from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    """ Newsletter form """
    class Meta:
        """ Newsletter metaform """
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            """ Clean email """
            email = self.cleaned_data.get('email')

            return email
