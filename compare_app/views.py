from rest_framework.response import Response

from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from main.data import category
from .scripts import *

from main.serializers import *
from main.models import *


class OneToOneView(APIView):
    def get(self, request, first_id, second_id, title):
        f_services = Service.objects.filter(tsj_id = first_id, breakdown = category[title])
        print(len(f_services))
        s_services = Service.objects.filter(tsj_id = second_id, breakdown = category[title])
        print(len(s_services))
        if f_services and s_services:
            cmp_obj = {}
            f_ser_data = ServiceSerializer(f_services, many = True).data
            s_ser_data = ServiceSerializer(s_services, many = True).data
            cmp_obj['avg_time'] = getCompareObjectsForWorkTime(f_ser_data, s_ser_data)
            cmp_obj['percent_of_done_works'] = getCompareObjectsOfReasonToCall(f_ser_data, s_ser_data)
            cmp_obj['total_mkd'] = getCompareObjectsOfTotalHouses(first_id, second_id)
            cmp_obj['total_area'] = getCompareObjectsOfTotalSquares(first_id, second_id)
            cmp_obj['global_rating'] = getCompareObjectsOfGlobalRating(first_id, second_id)
            return Response(cmp_obj)
        else:
            return Response({'data':'data is not found'})

class WorksToPeriodView(APIView):
    def get(self, request, id, title, start_period, end_period):
        services = Service.objects.filter(tsj_id = id, breakdown = category[title])
        if services:
            ser_data = ServiceSerializer(services, many = True).data
            res = getWorksOnPeriod(ser_data, start_period, end_period)
            return Response(res)
        else:
           return Response({'data':'data is not found'}) 




