from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from app.models import *

# Create your views here.
def sites(request):
    #return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>')
    sites = IP.objects.all();
    return render_to_response('app/tunnel.html', { 'sites' : sites })

def home(request):
    return HttpResponse('<html><head><title>Home!</title></head><body><h1>Home Sweet Home</h1></body></html>')
