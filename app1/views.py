from django.shortcuts import render
from django.http import HttpResponse


def set_cookie(request):
    resp = HttpResponse('<h1>cookie set</h1>')
    resp.set_cookie('mode', 'dark', max_age=60)
    return resp


def get_cookie(request):
    user_preference = request.COOKIES['mode']
    return HttpResponse(f'<h1>{user_preference}</h1>')
