from django.contrib import admin
from django import forms

from .models import (About, )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


