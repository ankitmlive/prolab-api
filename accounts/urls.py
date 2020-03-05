from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('register/', views.RegisterView.as_view(), name='register-user'),
]