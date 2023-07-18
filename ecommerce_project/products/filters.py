import django_filters

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    """
    filter for product.
    """
    name = django_filters.CharFilter(lookup_expr='icontains')  # filter if abc jacket and if user entered only abc then
    # also show the result

    class Meta:
        model = Product
        fields = {'name'}

