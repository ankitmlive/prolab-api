from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListAPIView.as_view(), name='article-list'),
    path('create/', views.ArticleCreateAPIView.as_view(), name='article-create'),
    url(r'^(?P<slug>[\w-]+)/$', views.ArticleDetailAPIView.as_view(), name='article-detail'),
]