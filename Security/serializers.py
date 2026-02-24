from rest_framework import serializers
from .models import SystemStatus, Patch

class SystemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemStatus
        fields = '__all__'

class PatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patch
        fields = '__all__'