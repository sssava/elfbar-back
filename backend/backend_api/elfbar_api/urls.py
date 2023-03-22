from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('elfbar-list/', ElfbarList.as_view(), name="elf-list"),
    path('product/<slug:slug>/', ElfbarGet.as_view(), name='elf-get'),
    path('tastes/<int:charge>/', ElfbarGetTastes.as_view(), name="tastes-get"),
    path('create_order/', CreateOrder.as_view(), name="create_order"),
    path('create_order_item/', CreateOrderItem.as_view(), name="create_order_item")
]

