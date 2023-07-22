from django.urls import path
from core.views import index_view, AddCcustomerView

urlpatterns = [
    path('', index_view, name='home'),
    path('add-customer', AddCcustomerView.as_view(), name='add')
]
