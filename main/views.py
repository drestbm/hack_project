from rest_framework.response import Response

from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from .data import category

from .serializers import *
from .models import *

class ServiceView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceByCompanyIdView(APIView):
    def get(self, request, pk):
        services = Service.objects.filter(tsj_id = pk)
        if services:
            serializer = ServiceSerializer(services, many = True)
            return Response(serializer.data)
        else:
            return Response({'data': 'not found'})

class ServiceByCompanyIdAndSlugView(APIView):
        def get(self, request, pk, title):
            services = Service.objects.filter(tsj_id = pk, breakdown = category[title])
            if services:
                serializer = ServiceSerializer(services, many = True)
                return Response(serializer.data)
            else:
                return Response({'data': 'not found'})

