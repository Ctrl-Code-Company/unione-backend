from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'is_finished']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        validated_data['is_finished'] = False
        return super().create(validated_data)
