from auditlog.registry import auditlog
from django.db import models

from users.models import User


# Create your models here.
class Category(models.Model):
    """model for the categories."""
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Create Product table for Products.
    """
    name = models.CharField(max_length=60)
    product_code = models.CharField(max_length=5)
    price = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    manufacture_date = models.DateTimeField(auto_now_add = True)
    expiry_date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name


auditlog.register(Category)
auditlog.register(Product)