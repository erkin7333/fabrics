from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .models import MenuCategory, Caregory, Product


def homepage(request):
    image = MenuCategory.objects.all()
    products = Product.objects.order_by('-created_at').exclude(top=True)
    top_product = Product.objects.filter(top=True)
    context = {
        'image': image,
        'products': products,
        'top_product': top_product
    }
    return render(request, 'main/index.html', context=context)

def menu_product(request, pk):
    menuproduct = Product.objects.filter(menucategoriy_id=pk)
    cart = Cart(request)
    print("Cart tekshiruv---------------->>>>>>>>>>>>>>", cart.get_total_cost())
    context = {
        'menuproduct': menuproduct
    }
    return render(request, 'product/menu-product.html', context=context)


class CategoryProduct(LoginRequiredMixin, TemplateView):
    template_name = 'product/category-product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        categoryproduct = Product.objects.filter(categories_id=pk)
        context['categoryproduct'] = categoryproduct
        return context

class SubcategoryProduct(LoginRequiredMixin, TemplateView):
    template_name = 'product/subcategory-product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        subproduct = Product.objects.filter(subcategories_id=pk)
        context['subproduct'] = subproduct
        return context

class NewProduct(LoginRequiredMixin, ListView):
    template_name = 'product/new-product.html'
    def get_queryset(self):
        return Product.objects.order_by('-created_at').exclude(top=True)

class TopProduct(LoginRequiredMixin, ListView):
    template_name = 'product/top-product.html'
    def get_queryset(self):
        return Product.objects.filter(top=True)

class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product/productdetail.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newproduct = products = Product.objects.order_by('-created_at').exclude(top=True)[0:3]
        context['newproduct'] = newproduct
        return context


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect("fabrics_main:view_cart")

def change_quantity(request, product_id):
    action = request.GET.get('action', '')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id, quantity, True)

    return redirect('fabrics_main:view_cart')

def remove_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('fabrics_main:view_cart')

def view_cart(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'card/card.html', context=context)

def productfilter(request):
    return render(request, 'product/productfilter.html')


class CartAllDeleteView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.save()
        return redirect('fabrics_main:view_cart')



def order(request):
    return render(request, 'card/order.html')

