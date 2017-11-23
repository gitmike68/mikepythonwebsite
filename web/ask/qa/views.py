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



