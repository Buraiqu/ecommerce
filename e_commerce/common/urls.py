from django.urls import path
from . import views
app_name='common'
urlpatterns = [
   path('',views.common_home,name='index'),
   path('admin',views.admin_login,name='admin_login'),
   path('seller',views.seller_login,name='seller_login'),
   path('custommer',views.customer_login,name='customer_login')
]