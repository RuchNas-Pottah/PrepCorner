# from django.contrib.auth.models import User
from django.db import models

class Resources(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Resource(models.Model):
    topic = models.ForeignKey(Resources, related_name='content', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    link = models.URLField(max_length=1000,null=True,blank=True)
    content = models.TextField()