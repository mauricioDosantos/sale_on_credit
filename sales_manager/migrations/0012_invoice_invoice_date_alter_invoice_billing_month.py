# Generated by Django 4.1 on 2022-08-15 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0011_alter_invoice_billing_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 25, 0, 26, 13, 672768)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='billing_month',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 15, 0, 26, 13, 672812)),
        ),
    ]
