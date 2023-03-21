from django.urls import path
from . import views

app_name = 'bookstore_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_book/', views.add_book, name='add_book'),
    path('list_customers/', views.list_customers, name='list_customers'),
    path('list_books/', views.list_books, name='list_books'),
    path('list_customers_json/', views.list_customers_json, name='list_customers_json'),

    # path('search_customers/', views.search_customers, name='search_customers'),
    # Add more URL patterns for other views here
]
