from .models import Cars, Photos
from rest_framework import serializers


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = (
            'id',
            'car_id',
            'photo'
        )


class CarsSerializer(serializers.ModelSerializer):

    photos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='photo'
    )

    class Meta:
        model = Cars
        fields = (
            'id',
            'sellerUsername',
            'adventType',
            'priceUSD',
            'description',
            'sellerName',
            'locationName',
            'year',
            'vin',
            'brand',
            'model',
            'generation',
            'engine_capacity',
            'engine_type',
            'transmition_type',
            'photos'
        )



