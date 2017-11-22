from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template


def test(request, *args, **kwargs):
    if len(args) > 0:
        num = args[0]
    else:
        num = "OK"

    t = get_template('index.html')
    html = t.render_to_response()

    return HttpResponse(html)
    # return HttpResponse(str(num))
