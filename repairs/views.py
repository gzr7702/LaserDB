from django.shortcuts import render, render_to_response
from django.core.context_processors import request
from django.http import response

# Create your views here.

def repair_home(request):
    return render_to_response('repair.html')

def repair_form(request):
    return render_to_response('repair_form.html')