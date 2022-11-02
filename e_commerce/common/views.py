from django.shortcuts import render

# Create your views here.
def common_home(request):
    return render(request,'common_templates/index.html')

def admin_login(request):
    return render(request,'common_templates/admin.html')   

def seller_login(request):
    return render(request,'common_templates/seller.html')   

def customer_login(request):
    return render(request,'common_templates/customer.html')