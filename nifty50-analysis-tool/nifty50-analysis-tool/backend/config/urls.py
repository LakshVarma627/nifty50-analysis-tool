from django.urls import path  
from apps.nifty_data.views import NiftyDataView  

urlpatterns = [  
    path('api/v1/nifty/', NiftyDataView.as_view(), name='nifty-data'),  
]  
