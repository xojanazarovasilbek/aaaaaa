from rest_framework import serializers
from .models import Sumka


class SumkaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sumka
        fields = '__all__'