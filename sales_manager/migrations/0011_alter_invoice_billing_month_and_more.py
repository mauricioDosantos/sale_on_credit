# Generated by Django 4.1 on 2022-08-15 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0010_remove_dividend_status_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='billing_month',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 15, 0, 18, 2, 519908)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
