from django.contrib import admin
from .models import Product, Enquiry
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','category','capacity','is_active','is_featured')
    list_filter = ('category','brand','is_active','is_featured')
    search_fields = ('name','brand','description')
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','phone','city','property_type','monthly_bill','status','created_at')
    list_filter = ('status','property_type','created_at')
    search_fields = ('name','phone','email','city')
    readonly_fields = ('created_at',)
