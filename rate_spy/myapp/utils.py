from django.utils import timezone
from .models import LinkSetting

def save_to_database(name, url, interval_in_minutes):
    link_setting = LinkSetting(
        name=name,
        url=url,
        created_at=timezone.now(),
        interval_in_minutes=interval_in_minutes
    )
    link_setting.save()

def process_form_data(cleaned_data):
    # Insert your method to process the form data here
    pass