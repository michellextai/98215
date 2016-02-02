from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blog(models.Model):
    # Use CharField to be character counter sensitive
    title = models.CharField(max_length = 100)
    context = models.TextField()
    after = models.DateTimeField()
    initial = models.DateTimeField()

    def __unicode__(self): # python 2.7
        return self.title  # python 2.7

#   For python 3+, do the following instead:
#   def __str__(self):
#       return self.title