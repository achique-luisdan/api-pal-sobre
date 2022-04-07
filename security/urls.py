from rest_framework.routers import SimpleRouter
from .views import CustomAuthToken
from django.urls import path

urlpatterns = [
  path('login', CustomAuthToken.as_view())
]