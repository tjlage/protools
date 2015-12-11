from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from app.models import IP
from django.core.exceptions import ObjectDoesNotExist
import csv

def home(request):
    ureachs = IP.objects.filter(reach = 'UNREACHABLE');
    return render_to_response('app/home.html', { 'ureachs' : ureachs })

def ping(request):
    pings = IP.objects.all()
    return render_to_response('app/ping.html', { 'pings' : pings })
