from django.contrib import admin

# Register your models here.
from .models import Customer, Book, Author, Publisher, Order, Bookauthor, Orderbook, Authorpublisher

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Order)
admin.site.register(Bookauthor)
admin.site.register(Orderbook)
admin.site.register(Authorpublisher)
