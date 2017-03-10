import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now =  timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
        # 최근에 발행된 Question인가 판단해주는 메서드

        # return :Boolean (맞는지 아닌지)

        # 자신의 비라행일자 >= 현재시각 -하루만큼 시간
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text