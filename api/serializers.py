# Serializers convert python model instance (objects) into Python dictionary
from rest_framework import serializers
from base.models import Item

# ModelSerializer generates the serializer automatically using Django models
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'