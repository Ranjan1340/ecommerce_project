# from django.urls import path
# from . import views
# from .views import add_to_cart, view_cart, remove_from_cart, checkout, order_history, product_list

# urlpatterns = [
#     path("", views.login_view, name="login"),
    # path("products/", views.product_list, name="product_list"),
    # path("cart/", views.cart_view, name="cart_view"),
    # path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    # path("checkout/", views.place_order, name="place_order"),
    # path("orders/", views.order_history, name="order_history"),


#     path('cart/', view_cart, name='view_cart'),
#     path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
#     path('cart/remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
#     path('checkout/', checkout, name='checkout'),
#     path('orders/', order_history, name='order_history'),
#     path('products/', product_list, name='product_list'),
# ]


from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, checkout, order_history, product_list, custom_login_view, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    # path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', order_history, name='order_history'),
    path('products/', product_list, name='product_list'),
    path('', custom_login_view, name='login'),
    path('logout/', user_logout, name='logout'),
]

