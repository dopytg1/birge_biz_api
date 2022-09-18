# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import VerifiedDeliverer

class VerifiedDelivererSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedDeliverer
        fields = ["name", "phone_number"]
