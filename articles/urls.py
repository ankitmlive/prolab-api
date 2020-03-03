from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('create/', views.ArticleCreate.as_view(), name='article-create'),
    url(r'^(?P<slug>[\w-]+)/$', views.ArticleDetailAPIView.as_view(), name='article-detail'),
]