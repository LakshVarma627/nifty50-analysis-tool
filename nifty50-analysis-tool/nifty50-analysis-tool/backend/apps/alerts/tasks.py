from celery import shared_task  
from django.core.mail import send_mail  
from django.conf import settings  

@shared_task  
def trigger_price_alert(user_email, message):  
    try:
        send_mail(  
            subject='Nifty 50 Alert',  
            message=message,  
            from_email=settings.DEFAULT_FROM_EMAIL,  
            recipient_list=[user_email],  
            fail_silently=False,  
        )  
    except Exception as e:
        # Log the exception or handle it as needed
        print(f"Failed to send email: {e}")
