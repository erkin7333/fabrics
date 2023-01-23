from django.contrib import admin
from .models import (MenuCategory, Caregory, SubCategory,
                     Brand, Product, Payment, Order, OrderItem, Delivery, Setting)


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


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    class Meta:
        model =Brand
admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'menucategoriy', 'categories', 'subcategories', 'brand',
                    'name', 'manufacturer', 'vendor_code', 'title', 'available', 'price', 'selling_price',
                    'top', 'created_at', 'subject', 'description', 'image')
    list_display_links = ('id', 'menucategoriy', 'categories', 'brand', 'name')
    search_fields = ('name', 'vendor_code')
    list_per_page = 4
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    list_display_links = ('id', 'name')
    class Meta:
        model = Payment
admin.site.register(Payment, PaymentAdmin)


class OrderItemIneLineAdmin(admin.TabularInline):
    model = OrderItem

class AuthoreAdmin(admin.ModelAdmin):
    inlines = [OrderItemIneLineAdmin]

admin.site.register(Order, AuthoreAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    class Meta:
        model = Delivery
admin.site.register(Delivery, DeliveryAdmin)



class SettingAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']

    class Meta:
        model = Setting
admin.site.register(Setting, SettingAdmin)