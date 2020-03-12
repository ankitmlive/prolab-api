from django.urls import include, path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('register/', views.RegisterView.as_view(), name='register-user'),
    path('verify-email/', views.VerifyEmailView.as_view(), name='verify-email'),
]