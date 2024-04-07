from django.db import models

# Create your models here.
class LinkSetting (models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    interval_in_hours = models.IntegerField(null=True)
    interval_in_minutes = models.IntegerField()