from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import (About, Delivery, Contact, Comment, PublicOffer,
                     Order, Branches, BranchDetail, Blog, BlogDetail)


class AboutModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = About
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    form = AboutModelForm
    list_per_page = 2

admin.site.register(About, AboutAdmin)


class DelivreyModelForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Delivery
        exclude = ('created_add',)


class DeliveryAdmin(admin.ModelAdmin):
    form = DelivreyModelForm

admin.site.register(Delivery, DeliveryAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'address', 'email')
    list_display_links = ('id', 'phone', 'address',)

    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)


class CommitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'content', 'url')
    list_display_links = ('id', 'title')
    class Meta:
        model = Comment
admin.site.register(Comment, CommitAdmin)


class PublicOfferForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = PublicOffer
        fields = '__all__'

class PublicOfferAdmin(admin.ModelAdmin):
    form = PublicOfferForm

admin.site.register(PublicOffer, PublicOfferAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title',)
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class BranchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'image')
    list_display_links = ('id', 'name')
    class Meta:
        model = Branches
admin.site.register(Branches, BranchesAdmin)


class BranchDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'phone', 'address', 'email', 'location')
    list_display_links = ('id', 'phone',)
    class Meta:
        model = BranchDetail
admin.site.register(BranchDetail, BranchDetailAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image')
    list_display_links = ('id', 'title')
    class Mete:
        model = Blog
admin.site.register(Blog, BlogAdmin)


class BlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = BranchDetail
        fields = '__all__'

class BlogDetailAdmin(admin.ModelAdmin):
    form = BlogForm

admin.site.register(BlogDetail, BlogDetailAdmin)