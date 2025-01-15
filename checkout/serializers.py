from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    items = serializers.CharField(max_length=100,help_text="String of items")
