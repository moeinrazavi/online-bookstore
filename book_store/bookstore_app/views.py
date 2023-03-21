from django.shortcuts import render, redirect
from django.http import JsonResponse
# from django.core import serializers
from django.db.models import Q
from .forms import CustomerForm, BookForm, AuthorForm, PublisherForm, OrderForm
# from .forms import CustomerForm, BookForm, AuthorForm, PublisherForm
from .models import Customer, Book, Author, Publisher, Order, Bookauthor, Orderbook, Authorpublisher

def home(request):
    return render(request, 'bookstore_app/home.html')

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore_app:home')
    else:
        form = CustomerForm()
    return render(request, 'bookstore_app/add_customer.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore_app:home')
    else:
        form = BookForm()
    return render(request, 'bookstore_app/add_book.html', {'form': form})

# def list_customers(request):
#     customers = Customer.objects.all()
#     return render(request, 'bookstore_app/list_customers.html', {'customers': customers})

def list_customers_json(request):
    search_query = request.GET.get('search_query', '')
    customers = Customer.objects.filter(
        Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
    )
    customers_data = list(customers.values('customer_id','first_name', 'last_name', 'email', 'phone_number'))
    return JsonResponse(customers_data, safe=False)

def list_customers(request):
    search_query = request.GET.get('search_query', '')
    customers = Customer.objects.filter(
        Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
    )
    context = {'customers': customers, 'search_query': search_query}
    return render(request, 'bookstore_app/list_customers.html', context)


def list_books(request):
    sort_by = request.GET.get('sort_by', 'price')
    price_range = request.GET.get('price_range', 'all')

    if sort_by == 'price_asc':
        books = Book.objects.order_by('price')
    elif sort_by == 'price_desc':
        books = Book.objects.order_by('-price')
    else:
        books = Book.objects.all()

    if price_range != 'all':
        min_price, max_price = price_range.split('-')
        books = books.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'books': books,
        'sort_by': sort_by,
        'price_range': price_range,
    }
    return render(request, 'bookstore_app/list_books.html', context)

# def search_customers(request):
#     query = request.GET.get('q', '')
#     customers = Customer.objects.filter(first_name__icontains=query) | Customer.objects.filter(last_name__icontains=query)
#     data = serializers.serialize('json', customers)
#     return JsonResponse(data, safe=False)

# def search_customers(request):
#     query = request.GET.get('q', '')
#     customers = Customer.objects.filter(first_name__icontains=query) | Customer.objects.filter(last_name__icontains=query)
#     data = serializers.serialize('json', customers)
#     return JsonResponse({'data': data}, safe=False)
# Add more views for other options
