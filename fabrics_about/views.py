from django.shortcuts import render
from .models import (About, Delivery, Contact, Comment, PublicOffer, Order, Branches, BranchDetail)



def aboutpage(request):
    about_post = About.objects.all()
    context = {
        'about_post': about_post
    }
    return render(request, 'about/about.html', context=context)

def deliverypage(request):
    deliver_page = Delivery.objects.all()
    context = {
        'deliver_page': deliver_page
    }
    return render(request, 'about/delivery.html', context=context)

def contactpage(request):
    contact_page = Contact.objects.all()
    context = {
        'contact_page': contact_page
    }
    return render(request, 'about/contact.html', context=context)

def reviewspage(request):
    commnent_page = Comment.objects.all()
    print("__________JHJJJJJJJJJJJJJJJJ----------------->>>>>>>>>>>>>>>>>>>>", commnent_page)
    context = {
        'commnent_page': commnent_page
    }
    return render(request, 'about/reviews.html', context=context)

def agreementpage(request):
    public_offer = PublicOffer.objects.all()
    context = {
        'public_offer': public_offer
    }
    return render(request, 'about/agreement.html', context=context)

def how_to_order_page(request):
    how_to_order = Order.objects.all()
    context = {
        'how_to_order': how_to_order
    }
    return render(request, 'about/how-to-order.html', context=context)

def filialypage(request):
    branches = Branches.objects.all()
    context = {
        'branches': branches
    }
    return render(request, 'about/filiallar.html', context=context)

def filiaydetailpage(request, pk):
    branch_detail = BranchDetail.objects.filter(branch_id=pk)
    context = {
        'branch_detail': branch_detail
    }
    return render(request, 'about/filialydetail.html', context=context)


def blogpage(request):
    return render(request, 'about/blog.html')


def blogdetailpage(request):
    return render(request, 'about/blogdetail.html')

