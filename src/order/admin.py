from django.contrib import admin
from .models import *


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'shipping_price', 'customer_name', 'last_change', 'is_deleted', 'address', 'total_price')
    search_fields = ("item", "customer_name", "address")


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'status', 'last_change', 'is_deleted')


class DiscountCouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'discount_id', 'customer_name', 'discount_is_active', 'last_change', 'is_deleted')
    search_fields = ("code",)


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DiscountCoupon, DiscountCouponAdmin)
