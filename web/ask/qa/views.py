from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.db import models


def test(request, *args, **kwargs):
    if len(args) > 0:
        num = args[0]
    else:
        num = "OK"
    context = dict()
    context['num'] = num
    return render_to_response('index.html')
    # return render_to_response('base.html', context)
    # return HttpResponse(str(num))


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
