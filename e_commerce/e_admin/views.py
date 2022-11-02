from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render(request,'e_admin_templates/homepage.html')

def admin_approve_sellers(request):
    return render(request,'e_admin_templates/approve_sellers.html')

def admin_view_sellers(request):
    return render(request,'e_admin_templates/view_sellers.html') 

def admin_view_custommers(request):
    return render(request,'e_admin_templates/view_customers.html')           

def admin_change_password(request):
    return render(request,'e_admin_templates/change_password.html')
