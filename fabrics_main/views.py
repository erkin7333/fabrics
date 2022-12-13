from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import DetailView, TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .models import MenuCategory, Caregory, Product, OrderItem, Brand, Order
from .forms import OrderModelForm
from django.db.models import Q


def homepage(request):
    """For home page"""
    image = MenuCategory.objects.all()
    products = Product.objects.order_by('-created_at').exclude(top=True)
    top_product = Product.objects.filter(top=True)
    context = {
        'image': image,
        'products': products,
        'top_product': top_product
    }
    return render(request, 'main/index.html', context=context)


class SearchResultView(ListView):
    """Search results class"""
    model = Product
    template_name = 'product/search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')

        object_list = Product.objects.filter(Q(name__icontains=query) | Q(title__icontains=query) | Q(subject__contains=query)
                                                 | Q(vendor_code__icontains=query))
        return object_list


class SelectSearchView(ListView):
    """Search items class"""
    model = Product
    template_name = 'product/select-search.html'

    def get_queryset(self):
        menucategory = self.request.GET.get('menucategory')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        min_price = self.request.GET.get('min_price', '')
        max_price = self.request.GET.get('max_price', '')
        if min_price == "":
            min_price = 0
        if max_price == "":
            max_price = 100000000000000000000000000
        object_list = Product.objects.filter(menucategoriy__id=menucategory, categories__id=category,
                                             brand__id=brand, price__range=(min_price, max_price))
        return object_list


@login_required
def menu_product(request, pk):
    """Fuction for menu products"""
    mencategory = MenuCategory.objects.all()
    brands = Brand.objects.all()
    menuproduct = Product.objects.filter(menucategoriy_id=pk)
    context = {
        'menuproduct': menuproduct,
        'mencategory': mencategory,
        'brands': brands
    }
    return render(request, 'product/menu-product.html', context=context)


def htmxcategory(request):
    """Using HTMX for check dropdown exist."""
    menu = request.GET.get('menucategory')
    categories = Caregory.objects.filter(menucategory=menu)
    context = {
        'categories': categories
    }
    return render(request, 'partials/categories.html', context=context)


@login_required
def brand_product(request, pk):
    """View for brand products."""
    brandproduct = Product.objects.filter(id=pk)
    context = {
        'brandproduct': brandproduct,
    }
    return render(request, 'product/brand-product.html', context=context)


class CategoryProduct(LoginRequiredMixin, TemplateView):
    """Find category on generics view."""
    template_name = 'product/category-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        categoryproduct = Product.objects.filter(categories_id=pk)
        mencategory = MenuCategory.objects.all()
        brands = Brand.objects.all()
        context['categoryproduct'] = categoryproduct
        context['mencategory'] = mencategory
        context['brands'] = brands
        return context



class SubcategoryProduct(LoginRequiredMixin, TemplateView):
    """Class for subcategory."""
    template_name = 'product/subcategory-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        subproduct = Product.objects.filter(subcategories_id=pk)
        context['subproduct'] = subproduct
        return context



class NewProduct(LoginRequiredMixin, ListView):
    """Filter new products."""
    template_name = 'product/new-product.html'

    def get_queryset(self):
        return Product.objects.order_by('-created_at').exclude(top=True)



class TopProduct(LoginRequiredMixin, ListView):
    """Find Top products."""
    template_name = 'product/top-product.html'

    def get_queryset(self):
        return Product.objects.filter(top=True)



class ProductDetailView(LoginRequiredMixin, DetailView):
    """Product detail class."""
    template_name = 'product/productdetail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newproduct = products = Product.objects.order_by('-created_at').exclude(top=True)[0:3]
        context['newproduct'] = newproduct
        return context




def add_to_cart(request, product_id):
    """Adding to cart func."""
    cart = Cart(request)
    cart.add(product_id)
    return redirect("fabrics_main:view_cart")



def change_quantity(request, product_id):
    """Change amount of the products."""
    action = request.GET.get('action', '')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id, quantity, True)

    return redirect('fabrics_main:view_cart')


def remove_cart(request, product_id):
    """Function for remove prodct from cart."""
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('fabrics_main:view_cart')


def view_cart(request):
    """Fuction for view cart."""
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'card/cart.html', context=context)


class CartAllDeleteView(View):
    """Delete all cart items view."""

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.save()
        return redirect('fabrics_main:view_cart')



def checkout(request):
    """Function for checkout product"""
    cart = Cart(request)
    if request.method == "POST":
        form = OrderModelForm(request.POST)
        if form.is_valid():

            total_price = 0
            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])
            order = form.save(commit=False)
            order.user = request.user
            order.paid_amount = total_price
            order.save()
            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity
                item = OrderItem.objects.create(order=order,
                                                product=product,
                                                total_price=price,
                                                quantity=quantity)
                item.save()
            cart.clear()
            return redirect('fabrics_main:my_orders')
    else:
        form = OrderModelForm()
    context = {
        'form': form,
        'cart': cart
    }
    return render(request, 'card/checkout.html', context=context)


def my_orders(request):
    """View for my orders filter"""
    ordet_items = OrderItem.objects.filter(order__user=request.user)
    context = {
        'ordet_items': ordet_items
    }
    return render(request, 'card/myorder.html', context=context)


def order_detail(request, pk):
    """For use order detail"""
    order = get_list_or_404(OrderItem, id=pk)
    context = {
        'order': order
    }
    return render(request, 'card/orderdetaile.html', context=context)