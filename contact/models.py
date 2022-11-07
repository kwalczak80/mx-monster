""" Contact app model """
from django.db import models


class Contact(models.Model):
    """ Models for the contact app """
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
