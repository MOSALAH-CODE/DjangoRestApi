from django.urls import path

from .views import (UpdateModelDetailAPIView, UpdateModelListAPIView)

urlpatterns = [
    path('<int:id>/', UpdateModelDetailAPIView.as_view(), name='update-model-list'),  # List all available updates for a
    path('', UpdateModelListAPIView.as_view(), name='update-model-list'),  # List all available updates for a
]
