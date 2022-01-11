from django.db import models

class Urls(models.Model):
    url = models.CharField(max_length=300, verbose_name='original url')
    shorter_url = models.CharField(max_length=200, verbose_name='shorter url')

