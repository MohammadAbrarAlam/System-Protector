from django.db import models

class SystemStatus(models.Model):
    cpu = models.FloatField()
    ram = models.FloatField()
    disk = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Patch(models.Model):
    system_name = models.CharField(max_length=100)
    patch_version = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)