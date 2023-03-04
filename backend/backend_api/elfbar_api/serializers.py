from rest_framework import serializers
from .models import *


class TasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taste
        fields = '__all__'


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = '__all__'


class ElfbarSerializer(serializers.ModelSerializer):
    taste = TasteSerializer(many=False)
    charge = ChargeSerializer(many=False)

    class Meta:
        model = Elfbar
        fields = '__all__'
