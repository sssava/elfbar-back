from rest_framework import serializers
from .models import *


class TasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taste
        fields = '__all__'


class ElfbarSerializer(serializers.ModelSerializer):
    taste = TasteSerializer(many=False)

    class Meta:
        model = Elfbar
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
