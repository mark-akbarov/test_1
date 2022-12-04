from django.db import models
from exam.models.question import Question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.option_text} - {self.is_correct}"