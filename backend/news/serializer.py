from rest_framework import serializers

from news.models import ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['url', 'title', 'description', 'thumbnail']
