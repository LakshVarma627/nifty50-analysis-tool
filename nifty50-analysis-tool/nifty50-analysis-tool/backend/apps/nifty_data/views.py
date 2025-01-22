from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import NiftyData  
from .serializers import NiftyDataSerializer  

class NiftyDataView(APIView):  
    def get(self, request):  
        # Fetch latest 100 records (example)  
        data = NiftyData.objects.all().order_by('-timestamp')[:100]  
        serializer = NiftyDataSerializer(data, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)  