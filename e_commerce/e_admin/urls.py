from django.urls import path
from . import views
app_name='e_admin'
urlpatterns = [
    path('',views.admin_home,name = 'homepage'),
    path('approve_sellers',views.admin_approve_sellers,name = 'approve_sellers'),
    path('view_sellers',views.admin_view_sellers,name = 'view_sellers'),
    path('view_cutomers',views.admin_view_custommers,name = 'view_customers'),
    path('change_password',views.admin_change_password,name = 'change_password')

]    