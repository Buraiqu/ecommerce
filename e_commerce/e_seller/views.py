from django.shortcuts import render

# Create your views here.
def e_seller_home(request):
    return render(request,'e_seller_templates/homepage.html')

def e_seller_add_product(request):
    return render(request,'e_seller_templates/add_product.html')

def e_seller_my_product(request):
    return render(request,'e_seller_templates/my_product.html') 

def e_seller_product_catalogues(request):
    return render(request,'e_seller_templates/product_catalogues.html')        

def e_seller_profile(request):
    return render(request,'e_seller_templates/profile.html')          

def e_seller_change_password(request):
    return render(request,'e_seller_templates/change_password.html')

def e_seller_update_stock(request):
    return render(request,'e_seller_templates/update_stock.html')    
