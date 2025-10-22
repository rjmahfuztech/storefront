from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

# Creating custom serializer fields
# Serializing relationships

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=260)
    price = serializers.DecimalField(max_digits=12, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    # collection = serializers.StringRelatedField() # another way to show the string of the collection
    # collection = CollectionSerializer() # another way to add nested object of the collection
    collection = serializers.HyperlinkedRelatedField(queryset=Collection.objects.all(), view_name='collection-detail')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)