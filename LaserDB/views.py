from django.shortcuts import render, render_to_response
from django.core.context_processors import request
from django.http import response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib import auth

@login_required
def home(request):
    return render_to_response('home.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')
    
def loggedin(request):
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})
    
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    return render_to_response('logout.html')
