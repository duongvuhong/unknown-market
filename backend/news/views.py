from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ArticleModel
from .serializer import ArticleSerializer


class ArticleList(APIView):
    """
    List all articles
    """
    def get(self, request, format=None):
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
