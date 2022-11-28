from fabrics_main.models import MenuCategory, Caregory, Collection, Brand



def dropdownmenu(request):
    menu_category = MenuCategory.objects.all()
    collection = Collection.objects.all()
    brand = Brand.objects.all()
    print("AAAAAAAAAAAAAAAA------------------>>>>>>>>>>>", menu_category)
    ctx = {
        'menu_category': menu_category,
        'collection': collection,
        'brand': brand
    }
    return ctx


