from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def test(request, *args, **kwargs):
    if len(args) > 0:
        num = args[0]
    else:
        num = "OK"
    return render_to_response('index.html')
    # return HttpResponse(str(num))
