# Generated by Django 4.1 on 2022-08-14 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0005_alter_sale_div_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='div_id',
            new_name='dividens',
        ),
    ]