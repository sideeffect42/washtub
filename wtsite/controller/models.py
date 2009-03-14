from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=128)
    ip_address = models.IPAddressField('Server IP Address')
    description = models.TextField('Description', blank=True)
    administrator = models.ManyToManyField(User, related_name='host_administrator',default=1)

class Setting(models.Model):
    value = models.CharField(max_length=128)
    data = models.CharField(max_length=255)

    hostname = models.ForeignKey('Host',default=1)
