from django.urls import path
from . import views
app_name='e_customer'
urlpatterns = [
    path('',views.e_customer_home,name = 'homepage'),
    path('cart',views.e_customer_cart,name = 'cart'),
    path('product_details',views.e_customer_product_details,name = 'product_details'),
    path('my_orders',views.e_customer_my_orders,name = 'my_orders'),
    path('view_profile',views.e_customer_view_profile,name = 'view_profile'),
    path('change_passwordd',views.e_customer_change_password,name = 'change_passwordd')

]    