from django.urls import path
from .views import *


app_name = "fabrics_main"


urlpatterns = [
    path('', homepage, name='homepage'),

    path('product/', productfilter, name='productfilter'),

    path('product-detail/', productdetail, name='productdetail'),

    path('add-to-card', addtocard, name='addtocard'),

    path('order/', order, name='order')
]