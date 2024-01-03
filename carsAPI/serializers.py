from .models import Cars
from rest_framework import serializers

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = (
            'id',
            'brand',
            'model',
            'year',
            'price',
            'photos'
        )