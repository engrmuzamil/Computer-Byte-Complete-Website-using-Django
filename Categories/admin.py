from django.contrib import admin
from .models import CATEGORY
# Register your models here.
class CATEGORYAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Category_Name',)}
    list_display = ('Category_Name','slug')
admin.site.register(CATEGORY,CATEGORYAdmin)
