from django.urls import path
from . import views

urlpatterns = [
    path('list-questions/', views.QuestionListAPIView.as_view()),
    path('create-question/', views.QuestionCreateAPIView.as_view()),
    path('rud-question/<int:pk>/', views.QuestionRUDAPIView.as_view()),
    path('list-answer/', views.AnswerListAPIView.as_view()),
    path('create-answer/', views.AnswerCreateAPIView.as_view()),
    path('rud-answer/<int:pk>/', views.AnswerRUDAPIView.as_view())
]
