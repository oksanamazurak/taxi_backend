from rest_framework import serializers
from .models import Client, Driver, Order

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'surname', 'phone_number']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'surname', 'phone_number', 'license_number', 'rating']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'start_address', 'final_address', 'driver_id', 'clients', 'km']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['driver_id'] = instance.driver_id.id
        return representation
