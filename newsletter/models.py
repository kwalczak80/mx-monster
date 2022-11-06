""" Newsletter model """
from django.db import models


class NewsletterUser(models.Model):
    """ Newsletter user model """
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Newsletter user model """
        return self.email
