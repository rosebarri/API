from rest_framework import serializers

class CurrencySerializer(serializers.Serializer):
    amount = serializers.FloatField()
