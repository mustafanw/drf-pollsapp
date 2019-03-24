from django.db import models
from django.utils import timezone
import datetime


class Track(models.Model):
    name = models.CharField(max_length=10, default="",null=True)
    def __str__(self):
        return self.name
class Question(models.Model):
    track = models.ForeignKey(Track,on_delete=models.CASCADE, default="",null=True)
    question_text = models.CharField(max_length=200, default="Enter",null=True)
    #pub_date = models.DateTimeField(blank=True,null=True, default="")
    #created_date = models.DateTimeField(default="",null=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default="",null=True)
    choice_text = models.CharField(max_length=200, default="",null=True)
    votes = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.choice_text
