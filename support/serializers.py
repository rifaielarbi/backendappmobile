from rest_framework import serializers
from .models import SupportRequest

class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = ['id', 'user', 'subject', 'message', 'created_at']
        read_only_fields = ['user','created_at']
