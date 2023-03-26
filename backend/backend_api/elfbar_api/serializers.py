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
    elfbar = serializers.PrimaryKeyRelatedField(queryset=Elfbar.objects.all())

    class Meta:
        model = OrderItem
        fields = ['elfbar', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['name', 'surname', 'postal_code', 'order_items']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for order_data in order_item_data:
            OrderItem.objects.create(order=order, **order_data)
        return order
