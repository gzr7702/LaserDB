from django.shortcuts import render, render_to_response
from django.core.context_processors import request
from django.http import response

# Create your views here.

def home(request):
    return render_to_response('home.html')