from django.contrib import admin
from django.urls import path
from .views import (RegisterAPIView, LoginAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
]
