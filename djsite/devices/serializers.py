from rest_framework import serializers
from .models import *


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['description_paragraph']


class IndexSerializer(serializers.ModelSerializer):
    cat = serializers.CharField(source='cat.category')
    description = DescriptionSerializer()

    class Meta:
        model = Device
        fields = ("id", "name", "cat", 'description')
    #
    # def get_description(self, obj):
    #     return Description.objects.filter(device=obj).first().description_paragraph if Description.objects.filter(
    #         device=obj.exists() else None

class SelectedDeviceSerializer(serializers.Serializer):
    card_id = serializers.IntegerField()