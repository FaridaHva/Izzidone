from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('created_at', 'is_active')

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())