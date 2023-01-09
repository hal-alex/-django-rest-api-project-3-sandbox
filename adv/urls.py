from django.urls import path
from .views import AdvListView

urlpatterns = [
    path('', AdvListView.as_view())
]