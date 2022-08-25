from django.contrib import admin
from .models import Entry, Sku, Supplier, SkuBrand
# Register your models here.
admin.site.register(Entry)
admin.site.register(Sku)
admin.site.register(Supplier)
admin.site.register(SkuBrand)
