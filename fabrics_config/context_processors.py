from fabrics_main.models import MenuCategory, Caregory, Collection, Brand, Setting



def dropdownmenu(request):
    menu_category = MenuCategory.objects.all()
    collection = Collection.objects.all()
    brand = Brand.objects.all()
    ctx = {
        'menu_category': menu_category,
        'collection': collection,
        'brand': brand
    }
    return ctx

def context_settings(request):
    phone = Setting.objects.get(key='phone').value,
    context = {
        'phone': phone
    }
    return context
