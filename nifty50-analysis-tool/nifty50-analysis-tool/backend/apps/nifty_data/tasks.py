from celery import shared_task
from .services import fetch_from_alpha_vantage

@shared_task
def fetch_nifty_data():
    data = fetch_from_alpha_vantage()  # Implement your API fetcher
    NiftyData.objects.create(**data)
    return f"Updated {len(data)} records"