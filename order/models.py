from django.db import models
from user.models import Subject, Account


class WorkType(models.Model):
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class Work(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, related_name='work_types')
    specialist = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='work_specialist')
    deadline = models.DateField()
    hours = models.CharField(max_length=15)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_faster = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def get_comment_count(self):
        return self.work_comments.count()


class FileWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='files_work')
    file = models.FileField(upload_to='file_works')

    def __str__(self):
        return self.work.name


class Comment(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='work_comments')
    message = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

