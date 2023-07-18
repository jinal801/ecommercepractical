from django.urls import path
from rest_framework import routers

from products.api import CategoryViewSet

from . import views

# router = routers.DefaultRouter()
# router.register(r'category/', CategoryViewSet)

urlpatterns = [
    path('products_detail/', views.productsDetail, name = 'productsdetail'),
]

# urlpatterns += router.urls