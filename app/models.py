from django.db import models
from django.utils import timezone

# Create your models here.

class IP(models.Model):
    date = models.CharField("Date", max_length=15)
    ip = models.GenericIPAddressField("IP")
    site = models.CharField("Site", max_length=50)
    tunName = models.CharField("Tunnel Name", max_length=50)
    tunType = models.CharField("Tunnel Type", max_length=3)
    reach = models.CharField("Reachable", max_length=5)

class Ping(models.Model):
    #reach = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
