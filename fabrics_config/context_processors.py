from fabrics_main.models import MenuCategory, Caregory, Brand, Setting
from fabrics_main.cart import Cart


def dropdownmenu(request):
    menu_category = MenuCategory.objects.all()
    brand = Brand.objects.all()
    ctx = {
        'menu_category': menu_category,
        'brand': brand
    }
    return ctx


def context_settings(request):
    cart = ''
    phone =''
    try:
        return {"phone": Setting.objects.get(key='phone').value,}

        cart = Cart(request)
    except:
        pass
    return {'phone': phone, 'cart': cart}
