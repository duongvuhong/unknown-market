# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from unknown_news.models import ArticleModel
from scrapy_djangoitem import DjangoItem

class ArticleItem(DjangoItem):
    django_model = ArticleModel
