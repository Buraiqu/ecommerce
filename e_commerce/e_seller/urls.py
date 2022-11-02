from django.urls import path
from . import views
app_name='e_seller'
urlpatterns = [
    path('',views.e_seller_home,name = 'homepage'),
    path('add_product',views.e_seller_add_product,name = 'add_product'),
    path('my_product',views.e_seller_my_product,name = 'my_product'),
    path('product_catalogues',views.e_seller_product_catalogues,name = 'product_catalogues'),
    path('profile',views.e_seller_profile,name = 'profile'),
    path('change_password',views.e_seller_change_password,name = 'change_password'),
     path('update_stock',views.e_seller_update_stock,name = 'update_stock')


]    