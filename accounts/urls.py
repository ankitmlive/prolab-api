from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('register/', views.RegisterView.as_view(), name='register-user'),
    path('get-token/', obtain_auth_token, name='get-token'),
]