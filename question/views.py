from rest_framework import generics
from .serializers import QuestionSerializer, QuestionListSerializer, AnswerSerializer
from .models import Question, Answer
from .permissions import IsOwnerOrReadOnly


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionListSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        answer = self.request.GET.get('is_answered')
        views = self.request.GET.get('views')
        if answer:
            queryset = queryset.filter(is_answered=True)
        if views:
            queryset = queryset.order_by('-views')
        return queryset


class QuestionRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerListAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
