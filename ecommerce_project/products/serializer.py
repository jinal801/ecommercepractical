from rest_framework import serializers

from products.constant import PRODUCT_CREATED_MSG
from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the categories."""

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the products."""
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    @staticmethod
    def get_owner(obj):
        return PRODUCT_CREATED_MSG.format(
                obj.owner,
                obj.owner.email if obj.owner else obj.owner)