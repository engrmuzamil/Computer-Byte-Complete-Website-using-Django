from django.contrib import admin
from .models import Orders,OrderDetail
# Register your models here.
class ProductInOrder(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('Order','Products','Qty','ProductPrice', 'UpdatedAt')
    extra = 0
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('Order','Products','Qty','ProductPrice', 'UpdatedAt')
    def order_id(self, obj):
        return obj.Order.orderID
    order_id.short_description = 'orderID'
    search_fields = ['order_id','Products','UpdatedAt']
    list_per_page=25
class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID','OrderTotal','PhoneNo','DeliverAddress'  ,'status', 'CreatedAt')
    list_filter = ['status','CreatedAt']
    search_fields = ['orderID','PhoneNo','DeliverAddress', 'CreatedAt']
    list_per_page=25
    inlines = [ProductInOrder]


admin.site.register(Orders,OrderAdmin)
admin.site.register(OrderDetail,OrderItemsAdmin)
