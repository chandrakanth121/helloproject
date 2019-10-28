from django.shortcuts import render
from django.http  import HttpResponse
import datetime

# Create your views here.
def time(request):
    date=datetime.datetime.now()
    msg=' <h2>hai guest,good evening,/h2>'
    msg=msg+'<h1>now time is:' +str(date) + '</h1>'
    return HttpResponse(msg)
