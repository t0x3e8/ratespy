from django.utils import timezone
from .models import LinkSetting
import requests
from bs4 import BeautifulSoup

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

def process_form_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the rating
    rating_element = soup.find('div', {'class': 'we-customer-ratings__averages'})
    rating = rating_element.find('span', {'class': 'we-customer-ratings__averages__display'}).text.strip()

    # Find the element containing the reviews count
    reviews_element = soup.find('div', {'class': 'we-customer-ratings__count'}).text.strip()
    reviews_count = int(reviews_element.split()[0])

    return rating, reviews_count