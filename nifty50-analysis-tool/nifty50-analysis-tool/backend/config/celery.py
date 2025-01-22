from celery import Celery
from django.conf import settings

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-nifty-data-every-5m': {
        'task': 'apps.nifty_data.tasks.fetch_nifty_data',
        'schedule': 300.0,  # 5 minutes
    },
}