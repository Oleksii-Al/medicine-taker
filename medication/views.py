from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def medication(request):
    return HttpResponse("Hello app!")