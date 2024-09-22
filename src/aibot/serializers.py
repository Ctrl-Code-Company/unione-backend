from rest_framework import serializers


class AIBotSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
