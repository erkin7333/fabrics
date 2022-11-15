from django.shortcuts import render

def homepage(request):
    return render(request, 'main/index.html')


def aboutpage(request):
    return render(request, 'about/about.html')

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


def productfilter(request):
    return render(request, 'product/productfilter.html')


def productdetail(request):
    return render(request, 'product/productdetail.html')

def addtocard(request):
    return render(request, 'card/card.html')


def order(request):
    return render(request, 'card/order.html')

