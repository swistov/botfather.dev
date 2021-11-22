from django.contrib import admin

from apps.product.models import Purchase, Item, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_published"]
    list_filter = ["price", "is_published"]
    search_fields = [
        "name",
    ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["buyer", "item", "amount", "phone_number", "successful"]
    list_filter = ["item", "successful"]
    search_fields = ["name", "item", "shipping_address", "phone_number", "receiver"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
