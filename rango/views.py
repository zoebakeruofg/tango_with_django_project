from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango may or may not say \"hey there\", depending on whether or not you are his partner")