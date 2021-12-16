from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Product_Name',)}
    def image_tag(self, obj):
        return format_html('<img src="{}" width=100px height=100px/>'.format(obj.Product_Image.url))

    image_tag.short_description = 'Product_Image'

    list_display = ('image_tag','Product_Name', 'Product_Category','Product_Qty', 'is_available','Product_Price', 'Updated_Date')
admin.site.register(Product, StoreAdmin)
