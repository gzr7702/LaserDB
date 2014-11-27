from django.shortcuts import render, render_to_response
from django.core.context_processors import request
from django.http import response
from service_orders.models import ServiceLog, Part
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    service_list = ServiceLog.objects.all()
    context = {'service_list':service_list}
    print(context)
    return render_to_response('service_orders.html', context)

@login_required
def service_order_form(request):
    return render_to_response('repair_form.html')

@login_required
def individual_report(request, rma_number):
    service_order = ServiceLog.objects.get(rma_number=rma_number)
    context = {'service_order':service_order}
    return render_to_response('individual_report.html', context)