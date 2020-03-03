from django.urls import path, url

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('create/', views.ArticleCreate.as_view(), name='article-create'),
   # url(r'^(?P<slug>[\w-]+)/$', article_detail, name='article-detail'),
]