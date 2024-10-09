from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def products(request):
    return render(request, 'dashboard/products.html')

@login_required(login_url='user-login')
def order(request):
    return render(request, 'dashboard/order.html')


