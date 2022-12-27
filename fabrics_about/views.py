from django.shortcuts import render
from .models import (About, Delivery, Contact, Comment, PublicOffer,
                     Order, Branches, BranchDetail, Blog, BlogDetail)



def aboutpage(request):
    """Function for about page."""
    about_post = About.objects.all()
    context = {
        'about_post': about_post
    }
    return render(request, 'about/about.html', context=context)


def deliverypage(request):
    """Delivery page view."""
    deliver_page = Delivery.objects.all()
    context = {
        'deliver_page': deliver_page
    }
    return render(request, 'about/delivery.html', context=context)


def contactpage(request):
    """Contect page view."""
    contact_page = Contact.objects.all()
    context = {
        'contact_page': contact_page
    }
    return render(request, 'about/contact.html', context=context)


def reviewspage(request):
    """Reviews page view."""
    commnent_page = Comment.objects.all()
    context = {
        'commnent_page': commnent_page
    }
    return render(request, 'about/reviews.html', context=context)


def agreementpage(request):
    """Agreement page function."""
    public_offer = PublicOffer.objects.all()
    context = {
        'public_offer': public_offer
    }
    return render(request, 'about/agreement.html', context=context)


def how_to_order_page(request):
    """Order page function."""
    how_to_order = Order.objects.all()
    context = {
        'how_to_order': how_to_order
    }
    return render(request, 'about/how-to-checkout.html', context=context)


def filialypage(request):
    """Branch page function."""
    branches = Branches.objects.all()
    context = {
        'branches': branches
    }
    return render(request, 'about/filiallar.html', context=context)


def filiaydetailpage(request, pk):
    """Branch detail page view."""
    branch_detail = BranchDetail.objects.filter(branch_id=pk)
    context = {
        'branch_detail': branch_detail
    }
    return render(request, 'about/filialydetail.html', context=context)


def blogpage(request):
    """Blog page function for get all."""
    blog_page = Blog.objects.all()
    context = {
        'blog_page': blog_page
    }
    return render(request, 'about/blog.html', context=context)


def blogdetailpage(request, pk):
    """Blog detail page function."""
    detail_blog = BlogDetail.objects.filter(blog_id=pk)
    context = {
        'detail_blog': detail_blog
    }
    return render(request, 'about/blogdetail.html', context=context)

