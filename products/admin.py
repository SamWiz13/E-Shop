from django.contrib import admin
from .models import *



class ProductImageInline(admin.TabularInline):
    model =ProductImage



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date', 'category', 'author')
    inlines = [ProductImageInline]


    
    

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Comment)

  