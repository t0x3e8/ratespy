from django.db import models
from django.utils import timezone

# Create your models here.
class LinkSetting (models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    interval_in_hours = models.IntegerField(null=True)
    interval_in_minutes = models.IntegerField()
    
class RatingRecord(models.Model):
    link_setting = models.ForeignKey('LinkSetting', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating_value = models.DecimalField(max_digits=5, decimal_places=2)
    review_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.link_setting.name} - {self.created_at}"