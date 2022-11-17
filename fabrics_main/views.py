from django.shortcuts import render

def homepage(request):
    return render(request, 'main/index.html')



def productfilter(request):
    return render(request, 'product/productfilter.html')


def productdetail(request):
    return render(request, 'product/productdetail.html')

def addtocard(request):
    return render(request, 'card/card.html')


def order(request):
    return render(request, 'card/order.html')

