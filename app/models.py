from django.db import models
from django.utils import timezone

# Create your models here.

class IP(models.Model):
    ip = models.GenericIPAddressField("IP")
    site = models.CharField("Site", max_length=50)
    tunn = models.CharField("Tunnel", max_length=50)

class Ping(models.Model):
    reach = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
