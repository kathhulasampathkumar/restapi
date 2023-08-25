from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def index(request):
    contex={
        'Status':200 , 'Message':"found OK",
    }
    return HttpResponse(contex)
