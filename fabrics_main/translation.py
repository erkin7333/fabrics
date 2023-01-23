from .models import  SubCategory, MenuCategory, Caregory, Product
from modeltranslation.translator import TranslationOptions, register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ['title', 'subject', 'description']

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ['name']

@register(MenuCategory)
class MenuCategoryTranslationOptions(TranslationOptions):
    fields = ['name']
    
@register(Caregory)
class CaregoryTranslationOptions(TranslationOptions):
    fields = ['name']