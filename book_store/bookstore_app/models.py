# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Author'


class Authorpublisher(models.Model):
    author = models.ForeignKey(Author, models.DO_NOTHING)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AuthorPublisher'
        unique_together = (('author', 'publisher'),)


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(unique=True, max_length=255)
    publication_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Book'


class Bookauthor(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'BookAuthor'
        unique_together = (('book', 'author'),)


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    order_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '`Order`'


class Orderbook(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'OrderBook'
        unique_together = (('order', 'book'),)


class Publisher(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Publisher'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookstoreAppAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'bookstore_app_author'


class BookstoreAppAuthorpublisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(BookstoreAppAuthor, models.DO_NOTHING)
    publisher = models.ForeignKey('BookstoreAppPublisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookstore_app_authorpublisher'


class BookstoreAppBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    isbn = models.CharField(unique=True, max_length=13)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey('BookstoreAppPublisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookstore_app_book'


class BookstoreAppBookauthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(BookstoreAppAuthor, models.DO_NOTHING)
    book = models.ForeignKey(BookstoreAppBook, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookstore_app_bookauthor'


class BookstoreAppCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        managed = False
        db_table = 'bookstore_app_customer'


class BookstoreAppOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    customer = models.ForeignKey(BookstoreAppCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookstore_app_order'


class BookstoreAppOrderbook(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.IntegerField()
    book = models.ForeignKey(BookstoreAppBook, models.DO_NOTHING)
    order = models.ForeignKey(BookstoreAppOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookstore_app_orderbook'


class BookstoreAppPublisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.CharField(unique=True, max_length=254)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bookstore_app_publisher'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
