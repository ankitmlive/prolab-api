#from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from articles.models import Article
from articles.serializers import ArticleListSerializer, ArticleCreateUpdateSerializer

class ArticleList(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    #filter_backends= [SearchFilter, OrderingFilter]
    #permission_classes = [AllowAny]
    #search_fields = ['title', 'content', 'user__first_name']
    #pagination_class = PostPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Article.objects.all() #filter(user=self.request.user)
        # query = self.request.GET.get("q")
        # if query:
        #     queryset_list = queryset_list.filter(
        #             Q(title__icontains=query)|
        #             Q(content__icontains=query)|
        #             Q(user__first_name__icontains=query) |
        #             Q(user__last_name__icontains=query)
        #             ).distinct()
        return queryset_list

class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    #def perform_create(self, serializer):
     #   serializer.save(user=self.request.user)
