# Generated by Django 4.1.5 on 2023-05-14 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_rename_discount_amount_globalsettings_discount_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='issuer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.issuer'),
        ),
    ]
