from django.contrib import admin

from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'owner', 'category')
    list_display = ('name', 'price')
    list_display_links = ('name', 'price') # by default first column is the list display link but we can customize or give another field as an link for the edit that record.
    list_filter = ('name', 'price', 'category__name', 'owner')  # filter by the fields.
    list_select_related = ['owner']
    list_per_page = 2  # list per page.
    search_fields = ('name', 'price', 'product_code')  # search


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
