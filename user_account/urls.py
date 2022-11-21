from django.urls import path
from .views import *


app_name = "user_account"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login')
]