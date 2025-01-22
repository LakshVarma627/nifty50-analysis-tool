import time
import json
from .models import NiftyData

def nifty_stream():
    last_id = None
    while True:
        data = NiftyData.objects.filter(id__gt=last_id).order_by('timestamp')
        if data.exists():
            last_id = data.last().id
            yield f"data: {json.dumps(list(data.values()))}\n\n"
        time.sleep(5)  # 5-second updates