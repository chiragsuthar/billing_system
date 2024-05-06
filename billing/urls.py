from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('items/', views.item_list, name='item_list'),
    path('items/new/', views.item_create, name='item_create'),
    path('items/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'), 
    path('bill/new/', views.bill_create, name='bill_create'),
    path('bill/<int:pk>/', views.bill_detail, name='bill_detail'),
    path('accounts/logout/', views.user_logout, name='logout'),
]
