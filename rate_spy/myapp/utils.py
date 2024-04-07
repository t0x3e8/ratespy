from django.utils import timezone
from .models import LinkSetting

def save_to_database(name, url, interval_in_minutes):
    if not LinkSetting.objects.filter(name=name, url=url, interval_in_minutes=interval_in_minutes).exists():
        link_setting = LinkSetting(
            name=name,
            url=url,
            created_at=timezone.now(),
            interval_in_minutes=interval_in_minutes
        )
        link_setting.save()
        return True
    else:
        return False

def process_form_data(cleaned_data):
    # Insert your method to process the form data here
    pass