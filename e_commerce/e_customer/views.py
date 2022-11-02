from django.shortcuts import render

# Create your views here.
def e_customer_home(request):
    return render(request,'e_customer_templates/homepage.html')

def e_customer_cart(request):
    return render(request,'e_customer_templates/cart.html')

def e_customer_my_orders(request):
    return render(request,'e_customer_templates/my_orders.html') 

def e_customer_view_profile(request):
    return render(request,'e_customer_templates/view_profile.html')        

def e_customer_product_details(request):
    return render(request,'e_customer_templates/product_details.html')          

def e_customer_change_password(request):
    return render(request,'e_customer_templates/change_password.html')
