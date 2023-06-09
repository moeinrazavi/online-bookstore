# Generated by Django 4.1.7 on 2023-03-21 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='Author',
        ),
        migrations.AlterModelTable(
            name='authorpublisher',
            table='AuthorPublisher',
        ),
        migrations.AlterModelTable(
            name='book',
            table='Book',
        ),
        migrations.AlterModelTable(
            name='bookauthor',
            table='BookAuthor',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='Customer',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
        migrations.AlterModelTable(
            name='orderbook',
            table='OrderBook',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='Publisher',
        ),
    ]
