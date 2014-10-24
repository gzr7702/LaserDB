from django.shortcuts import render, render_to_response
from django.core.context_processors import request
from django.http import response
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render_to_response('home.html')