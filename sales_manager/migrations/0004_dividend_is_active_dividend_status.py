# Generated by Django 4.1 on 2022-08-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0003_remove_sale_div_id_sale_div_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='dividend',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dividend',
            name='status',
            field=models.CharField(choices=[('Atrasado', 'Atrasado'), ('Em dias', 'Em dias'), ('A vencer', 'A vencer')], default='Em dias', max_length=20),
        ),
    ]
