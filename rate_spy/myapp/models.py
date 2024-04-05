from django.db import models

# Create your models here.
class LinkSetting (models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    interval_in_min = models.IntegerField()