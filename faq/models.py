from django.db import models


class Faq(models.Model):
    """
    The question and answer model
    """
    question = models.CharField(max_length=254)
    answer = models.TextField(blank=True)

    def __str__(self):
        """
        Return the question
        """
        return self.question


