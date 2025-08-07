from django.contrib import admin
from .models import Order
admin.site.register(Order)
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','total_amount','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('customer__username',)
