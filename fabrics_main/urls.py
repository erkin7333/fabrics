from django.urls import path
from .views import *


app_name = "fabrics_main"


urlpatterns = [
    path('', homepage, name='homepage'),

    path('about/', aboutpage, name='aboutpage'),

    path('delivery/', deliverypage, name='deliverypage'),

    path('contant/', contactpage, name='contactpage'),

    path('reviews/', reviewspage, name='reviewspage'),

    path('agreement/', agreementpage, name='agreementpage'),

    path('how_to_order_page/', how_to_order_page, name='how_to_order'),

    path('filialy/', filialypage, name='filialypage'),

    path('filialy-detail/', filiaydetailpage, name='filiaydetail'),

    path('blog/', blogpage, name='blogpage'),

    path('blog-detail/', blogdetailpage, name='blogdetail'),

    path('product/', productfilter, name='productfilter'),

    path('product-detail/', productdetail, name='productdetail'),

    path('add-to-card', addtocard, name='addtocard'),

    path('order/', order, name='order')
]