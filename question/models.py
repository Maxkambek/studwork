from django.db import models
from user.models import Account, Subject


class Question(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject_question = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_questions')
    question = models.TextField()
    image = models.ImageField(upload_to='questions/', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    user = models
