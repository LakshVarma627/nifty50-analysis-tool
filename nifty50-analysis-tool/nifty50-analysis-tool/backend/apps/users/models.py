from django.contrib.auth.models import AbstractUser  
from django.db import models  

class CustomUser(AbstractUser):  
    phone = models.CharField(max_length=15, blank=True, null=True)  
    alert_preferences = models.JSONField(  
        default=dict,  
        help_text="User preferences for alerts (e.g., {'email': True, 'sms': False})"  
    )  

    def __str__(self):  
        return self.email  