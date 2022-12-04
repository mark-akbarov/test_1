from django.db import models
from exam.models.question import Question


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    question = models.ManyToManyField(Question)
    
    def __str__(self) -> str:
        return self.title