# Generated by Django 4.1 on 2022-08-14 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0006_rename_div_id_sale_dividens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='dividens',
        ),
        migrations.AddField(
            model_name='sale',
            name='div_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='sales_manager.dividend'),
            preserve_default=False,
        ),
    ]