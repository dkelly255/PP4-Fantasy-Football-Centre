import datetime

from django.db import models
from django.utils import timezone


# Credits - this code is sourced from the official Django documentation
# tutorials and is fully accredited in readme credits
# Create your models here.
class Question(models.Model):
    """
    The Question Model with attributes for content and dates
    and methods to display the question text and pulication date
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    The Choice Model with attributes for text and votes, a foreign key
    to the question model and methods to display the choice text
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
