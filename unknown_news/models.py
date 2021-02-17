from django.db import models

class ArticleModel(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=1000)
