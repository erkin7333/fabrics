from django.urls import path
from .views import *


app_name = "fabrics_about"


urlpatterns = [
    path('about/', aboutpage, name='aboutpage'),

    path('delivery/', deliverypage, name='deliverypage'),

    path('contant/', contactpage, name='contactpage'),

    path('reviews/', reviewspage, name='reviewspage'),

    path('agreement/', agreementpage, name='agreementpage'),

    path('how_to_order_page/', how_to_order_page, name='how_to_order'),

    path('filialy/', filialypage, name='filialypage'),

    path('filialy-detail/<int:pk>/', filiaydetailpage, name='filiaydetail'),

    path('blog/', blogpage, name='blogpage'),

    path('blog-detail/<int:pk>/', blogdetailpage, name='blogdetail'),
]