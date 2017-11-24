from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added-at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    author = models.ForeignKey(User, null=True, related_name='users_question')
    likes = models.ForeignKey(User, null=True, related_name='users_likes')
    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    # question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    question = models.ForeignKey(Question, null=True)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/answer/%d/' % self.pk


'''
class Post(models.Model):  # 1
    title = models.CharField(max_length=255)  # 2
    content = models.TextField()  # 3
    creation_date = models.DateTimeField(blank=True)  # 4

    def __unicode__(self):  # 5
        return self.title  # 6

    def get_absolute_url(self):  # 7
        return '/question/%d/' % self.pk  # 8

    class Meta:  # 9
        db_table = 'qa__question'  # 10
        ordering = ['-creation_date']  # 11
'''
