from django.contrib import admin
from .models import Cart, CartItems
from django.utils.html import format_html
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    def total(self, cart,total=0):
        cart_items = CartItems.objects.filter(cart=cart,IsActive=True)
        for cart_item in cart_items:
            total  +=  (cart_item.product.Product_Price * cart_item.Quantity)
        return total
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100px height=100px/>'.format(obj.product.Product_Image.url))
    def subtotal(self, obj):
        return obj.Quantity * obj.product.Product_Price
    image_tag.short_description = 'Product Image'
    subtotal.short_description = 'Net Amount'
    total.short_description = 'Total'
    list_display = ('Cart_ID','Date_Added','total')
    search_fields = ['Cart_ID' ]

class CartItemsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100px height=100px/>'.format(obj.product.Product_Image.url))
    def subtotal(self, obj):
        return obj.Quantity * obj.product.Product_Price

    image_tag.short_description = 'Product Image'
    subtotal.short_description = 'Net Amount'
    list_display = ('image_tag','product','Quantity','user', 'subtotal')
admin.site.site_header = ''
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
