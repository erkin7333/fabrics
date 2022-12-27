from django.urls import path
from .views import *


app_name = "fabrics_main"


urlpatterns = [
    path('', homepage, name='homepage'),

    path('search/', SearchResultView.as_view(), name='search'),

    path('select-search/', SelectSearchView.as_view(), name='select_search'),

    path('newproduct/', NewProduct.as_view(), name='newproduct'),

    path('top-product/', TopProduct.as_view(), name='top_product'),

    path('brand-product/<int:pk>/', brand_product, name='brand_product'),

    path('menu-product/<int:pk>/', menu_product, name='menu_product'),

    path('category-product/<int:pk>/', CategoryProduct.as_view(), name='category_product'),

    path('subcategory-product/<int:pk>/', SubcategoryProduct.as_view(), name='subproduct'),

    path('detail-product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),

    path('add-to-cart/<int:product_id>/', add_to_cart, name='addtocard'),

    path('change-quantity/<int:product_id>/', change_quantity, name='change_quantity'),
    
    path('remove-cart/<int:product_id>/', remove_cart, name='remove_cart'),

    path('delete-cart/', delete_all, name='delete_all'),

    path('view-cart/', view_cart, name='view_cart'),

    path('order/', checkout, name='order'),

    path('my-orders', my_orders, name='my_orders'),

    path('order-detail/<int:pk>/', order_detail, name='order_detail'),

    path('htmxcategory/', htmxcategory, name='htmxcategory')
]