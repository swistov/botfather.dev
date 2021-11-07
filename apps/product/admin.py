from django.contrib import admin

from apps.product.models import Purchase, Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category_name", "subcategory_name"]
    list_filter = ["price", "category_code", "category_name", "subcategory_code", "subcategory_name"]
    search_fields = ["name",]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["buyer", "item", "amount", "phone_number", "successful"]
    list_filter = ["item", "successful"]
    search_fields = ["name", "item", "shipping_address", "phone_number", "receiver"]
