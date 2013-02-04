#encoding: utf-8

from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return self.title