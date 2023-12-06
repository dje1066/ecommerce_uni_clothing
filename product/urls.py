from django.urls import path
from . import views
from .views import AddToCart, ProductView, index


urlpatterns = [
    path('', index),
    path('product-view/', ProductView.as_view(), name='product_view'),
    path('add-to-cart/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('change-quantity/<str:product_id>', views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<str:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]