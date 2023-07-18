from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.response import Response

from products.constant import PRODUCT_DELETED_MSG
from products.models import Category, Product
from products.serializer import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Ensure we have the authorized user for ownership."""
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """destroy the product and display the success message."""
        instance = self.get_object()
        if request.user == instance.owner:
            self.perform_destroy(instance)
            return Response({
                "message": PRODUCT_DELETED_MSG
            }, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()