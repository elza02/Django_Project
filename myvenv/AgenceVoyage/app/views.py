from django.shortcuts import render
from django.http import HttpResponse,request
def home (request):
    return HttpResponse("hello its me!")
# Create your views here.
