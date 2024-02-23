from django.urls import path

from .views import (
    StatusAPIView,
    # StatusListSearchAPIView,
    StatusDetailAPIView,
    # StatusCreateAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
    )

urlpatterns = [
    path('', StatusAPIView.as_view()), 
    # path('', StatusListSearchAPIView.as_view()), 
    path('<int:pk>/', StatusDetailAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()), 
    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]
