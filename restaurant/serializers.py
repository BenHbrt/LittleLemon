from rest_framework import serializers
from .models import Menu, BookingTable

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

class bookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = "__all__"