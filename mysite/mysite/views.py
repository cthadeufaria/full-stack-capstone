# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    html = '<html><body>Hello a41e8464</body></html>'
    return HttpResponse(html)