from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<title> A'Yanna's First Django Page </title><h1>A'Yanna Rouse </h1><h3> 23102274 </h3> <p> Django is okay, could be better!</p>")







