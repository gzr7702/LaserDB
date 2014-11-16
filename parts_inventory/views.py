from parts_inventory.models import Part
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def parts_home(request):
    parts_list = Part.objects.all()
    context = {'parts_list':parts_list}
    return render_to_response('parts.html', context)

@login_required
def parts_report(request, serial_number):
    part = Part.objects.get(serial_number=serial_number)
    context = {'part':part}
    return render_to_response('part_report.html', context)
