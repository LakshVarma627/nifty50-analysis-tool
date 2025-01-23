from celery import shared_task
from .services import fetch_from_alpha_vantage
from .models import NiftyData

@shared_task
def fetch_nifty_data():
    data = fetch_from_alpha_vantage()  # Implement your API fetcher
    NiftyData().insert_data(data)
    return f"Updated {len(data)} records"
