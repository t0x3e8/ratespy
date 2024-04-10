# tasks.py
from celery import shared_task
from .models import LinkSetting, RatingRecord
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from datetime import datetime

@shared_task
def update_ratings():
    link_settings = LinkSetting.objects.all()
    current_time = datetime.now().time()
    
    for setting in link_settings:
        # Check if the current time is a multiple of interval_in_minutes for this setting
        if current_time.minute % setting.interval_in_minutes == 0:
            # If it is, enqueue the update_ratings_and_reviews task with the link_setting_id
            update_ratings_and_reviews(setting.id)

def update_ratings_and_reviews(link_setting_id):
    link_setting = LinkSetting.objects.filter(id=link_setting_id).first()
    if link_setting:
        rating, reviews_count = process_link_setting_data(link_setting_id)
    
        # Save the rating record
        record_log = RatingRecord.objects.create(
            link_setting_id = link_setting_id,
            rating_value = rating,
            review_count = reviews_count
        )
        try:
            record_log.save()
            print("Rating record saved successfully!")
        except Exception as e:
            print(f"Error saving record_log: {e}")
    else:
        print(f"LinkSetting with id {link_setting_id} not found.")

def process_link_setting_data(link_setting_id):
    link_setting = LinkSetting.objects.get(id=link_setting_id)
    response = requests.get(link_setting.url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing the rating
    rating_element = soup.find('div', {'class': 'we-customer-ratings__averages'})
    rating = rating_element.find('span', {'class': 'we-customer-ratings__averages__display'}).text.strip()

    # Find the element containing the reviews count
    reviews_element = soup.find('div', {'class': 'we-customer-ratings__count'}).text.strip()
    reviews_count = int(reviews_element.split()[0])
    
    return rating, reviews_count