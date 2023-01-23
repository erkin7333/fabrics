from django.urls import path
from .views import *


app_name = "user_account"

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),

    path('login/', user_login, name='login'),

    path('logout/', user_logout, name='logout')
]