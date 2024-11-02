from rest_framework import serializers
from .models import Turn


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'
