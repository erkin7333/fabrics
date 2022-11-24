from django.contrib import admin
from .models import (MenuCategoriy, Caregoriy)


class MenuCategoriyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    class Meta:
        model = MenuCategoriy
admin.site.register(MenuCategoriy, MenuCategoriyAdmin)


class CategoriyAdmin(admin.ModelAdmin):
    list_display = ('id', 'menucategoriy', 'parent', 'name')
    list_display_links = ('id', 'menucategoriy', 'name')
    class Meta:
        model = Caregoriy
admin.site.register(Caregoriy, CategoriyAdmin)
