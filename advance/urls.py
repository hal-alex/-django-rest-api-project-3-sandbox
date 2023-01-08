from django.urls import path # import path to specify an endpoint
from .views import AdvanceListView, AdvanceDetailView # import view to attach to an endpoint

urlpatterns = [
    path('', AdvanceListView.as_view()), 
    path('<int:pk>/', AdvanceDetailView.as_view())
]