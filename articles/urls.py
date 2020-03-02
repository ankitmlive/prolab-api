from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('create/', views.ArticleCreate.as_view(), name='article-create'),
]