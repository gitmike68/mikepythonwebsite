from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def test(request, *args, **kwargs):
    num = len(args)
    return HttpResponse(str(num))
