# Generated by Django 4.1.7 on 2023-03-21 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0003_alter_author_table_alter_authorpublisher_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='`Order`',
        ),
    ]