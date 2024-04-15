from django.contrib import admin
from .models import LinkSetting, RatingRecord

# Register your models here.
admin.site.register(LinkSetting)
admin.site.register(RatingRecord)