from django.contrib import admin
from .models import (MenuCategory, Caregory, SubCategory,
                     Collection, Brand, Product, Payment, Order, OrderItem, Delivery, Setting)


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
    list_display = ('id', 'menucategoriy', 'categories', 'subcategories', 'collection', 'brand',
                    'name', 'manufacturer', 'vendor_code', 'title', 'available', 'price',
                    'top', 'created_at', 'subject', 'description', 'image')
    list_display_links = ('id', 'menucategoriy', 'categories', 'collection', 'brand', 'name')
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

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'payment_type', 'full_name', 'phone', 'email',
#                     'address', 'paid_amount', 'created_at', 'delivery')
#     list_display_links = ('id', 'user', 'payment_type', 'full_name')
#     class Meta:
#         model = Order
# admin.site.register(Order, OrderAdmin)
#
#
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order', 'product', 'total_price', 'quantity')
#     list_display_links = ('id', 'order', 'product')
#     class Meta:
#         model = OrderItem
# admin.site.register(OrderItem, OrderItemAdmin)

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