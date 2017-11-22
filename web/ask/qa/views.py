from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.loader import get_template


def test(request, *args, **kwargs):
    if len(args) > 0:
        num = args[0]
    else:
        num = "OK"

    # t = get_template('index.html')
    html = render_to_response('index.html')

    return html
    # return HttpResponse(str(num))
