from django.db import models


class ArticleModel(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    thumbnail = models.URLField(max_length=200)

    def __str__(self) -> str:
        return f'{self.title}'
