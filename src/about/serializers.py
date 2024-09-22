from rest_framework import serializers

from .models import About


class AboutSerializer(serializers.ModelSerializer):
    """About US serializer"""

    class Meta:
        model = About
        fields = ['body']
