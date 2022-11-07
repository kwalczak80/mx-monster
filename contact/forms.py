""" Form for the contact app """
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Form for the contact model
    """
    class Meta:
        """ Meta for the contact form """
        model = Contact
        fields = '__all__'
