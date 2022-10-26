from django.urls import path
from . import views

urlpatterns = [
    path('project-list/', views.MarketListAPIView.as_view()),
    path('project-create/', views.MarketCreateAPIView.as_view()),
    path('market-full-create/', views.MarketCreateView.as_view()),
    path('file-demo-create/', views.MarketFileDemoCreateAPIView.as_view()),
    path('file-done-create/', views.MarketFileDoneCreateAPIView.as_view()),
    path('market-rud/<int:pk>/', views.MarketRUDAPIView.as_view()),
]
