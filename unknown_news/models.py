from django.db import models

class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=500)
