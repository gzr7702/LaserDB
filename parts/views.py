from django.shortcuts import render, render_to_response

def parts_home(request):
    return render_to_response('parts.html')