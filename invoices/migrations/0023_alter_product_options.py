# Generated by Django 4.2.3 on 2023-09-24 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0022_alter_address_city_alter_address_postal_code_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
    ]
