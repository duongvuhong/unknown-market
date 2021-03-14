from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ArticleModel
from .serializer import ArticleSerializer


class ArticleList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = ArticleModel.objects.all()
        serializer = ArticleSerializer(snippets, many=True)
        return Response(serializer.data)
