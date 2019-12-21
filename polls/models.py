import datetime

from django.db import models
from django.utils import timezone

'''
Two models: Question and Choice
Question: question and a publication date
Choice: the text of the choice and a vote tally
Each Choice is associated with a Question
'''
'''
each model is represented by a class that subclasses django.db.models.Model
each model has a number of class variables, each of which represents a db field in the model
'''

'''
为这个应用创建数据库schema(生成CREATE TABLE语句)
创建可以与Question和Choice对象进行交交互的python db API
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text  #在数据库中更直观地输出<QUerySet [Question:  ]>

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#每个Choice对象都关联到一个Question对象
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text     #Django自动生成的admin使用这个方法来表示对象

