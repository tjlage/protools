from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from app.models import IP
from django.core.exceptions import ObjectDoesNotExist
import csv
# Create your views here.
def sites(request):
    #return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>')
    sites = IP.objects.all();
    return render_to_response('app/tunnel.html', { 'sites' : sites })

def home(request):
    return HttpResponse('<html><head><title>Home!</title></head><body><h1>Home Sweet Home</h1></body></html>')

def ping(request):
    dataReader = csv.reader(open("app/result/ping sample.csv"), delimiter=',')

    for row in dataReader:
        if row[0] != 'Date/Time': # Ignore the header row, import everything else
            ping = IP()
            ping.date = row[0]
            ping.site = row[1]
            ping.tunName = row[2]
            ping.tunType = row[3]
            ping.ip = row[4]
            ping.reach = row[5]
            
            dtexists = IP.objects.filter(date__iexact = ping.date).exists()
            diexists = IP.objects.filter(ip__iexact = ping.ip).exists()

            if not diexists:
                    ping.save()
            else:
                pass

        pings = IP.objects.all()

    return render_to_response('app/ping.html', { 'pings' : pings })
