from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('products/', views.products, name='dashboard-products'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('order/', views.order, name='dashboard-order'),
]