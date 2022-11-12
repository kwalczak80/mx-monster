from datetime import datetime
from django.db import models


class Staff(models.Model):
    """
    The Staff model
    """
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default='')
    photo = models.ImageField(null=True, blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        """
        Return the staff name
        """
        return self.name
