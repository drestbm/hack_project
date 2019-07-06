from rest_framework import serializers

from .models import *

class ServiceSerializer(serializers.ModelSerializer):
    man_company = serializers.StringRelatedField()
    class Meta:
        model = Service
        fields = ('tsj_id', 'house_id','name', 'address', 'breakdown', 'challenge_accepted', 'challenge_done', 'man_company', 'status')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account