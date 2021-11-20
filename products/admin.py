from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)