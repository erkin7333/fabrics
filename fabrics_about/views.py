from django.shortcuts import render
from .models import (About, )



def aboutpage(request):
    about_post = About.objects.all()
    context = {
        'about_post': about_post
    }
    return render(request, 'about/about.html', context=context)

def deliverypage(request):
    return render(request, 'about/delivery.html')

def contactpage(request):
    return render(request, 'about/contact.html')

def reviewspage(request):
    return render(request, 'about/reviews.html')

def agreementpage(request):
    return render(request, 'about/agreement.html')

def how_to_order_page(request):
    return render(request, 'about/how-to-order.html')

def filialypage(request):
    return render(request, 'about/filiallar.html')

def filiaydetailpage(request):
    return render(request, 'about/filialydetail.html')


def blogpage(request):
    return render(request, 'about/blog.html')


def blogdetailpage(request):
    return render(request, 'about/blogdetail.html')

