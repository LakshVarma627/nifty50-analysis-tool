from rest_framework import serializers  
from .models import NiftyData  

class NiftyDataSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = NiftyData  
        fields = ['timestamp', 'open', 'close', 'high', 'low', 'volume']  