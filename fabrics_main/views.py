from django.shortcuts import render
from .models import MenuCategory, Caregory

def homepage(request):
    image = MenuCategory.objects.all()
    # menu_category = MenuCategory.objects.all()
    context = {
        # 'menu_category': menu_category,
        'image': image
    }
    return render(request, 'base.html', context=context)



def productfilter(request):
    return render(request, 'product/productfilter.html')


def productdetail(request):
    return render(request, 'product/productdetail.html')

def addtocard(request):
    return render(request, 'card/card.html')


def order(request):
    return render(request, 'card/order.html')

