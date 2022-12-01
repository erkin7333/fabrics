from django.contrib import admin
from .models import (MenuCategory, Caregory, SubCategory,
                     Collection, Brand, Product)


class MenuCategoriyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    class Meta:
        model = MenuCategory
admin.site.register(MenuCategory, MenuCategoriyAdmin)


class CategoriyAdmin(admin.ModelAdmin):
    list_display = ('id', 'menucategory', 'name')
    list_display_links = ('id', 'menucategory', 'name')
    class Meta:
        model = Caregory
admin.site.register(Caregory, CategoriyAdmin)


class SubCategoriyAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name')
    list_display_links = ('id', 'category', 'name')
    class Meta:
        model = SubCategory
admin.site.register(SubCategory, SubCategoriyAdmin)









class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    class Meta:
        model = Collection

admin.site.register(Collection, CollectionAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    class Meta:
        model =Brand
admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'menucategoriy', 'categories', 'collection', 'brand',
                    'name', 'manufacturer', 'vendor_code', 'title', 'available',
                    'top', 'created_at')
    list_display_links = ('id', 'menucategoriy', 'categories', 'collection', 'brand', 'name')
    search_fields = ('name', 'vendor_code')
    list_per_page = 4
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
