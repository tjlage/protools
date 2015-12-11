import os, sys
import csv
proj_path = "/Users/tom/Documents/projects"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from app.models import IP
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
