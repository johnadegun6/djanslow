from django.urls import path
from core.views import index_view, add_customer

urlpatterns = [
    path('', index_view, name='home'),
    path('add-customer', add_customer, name='add')
]
