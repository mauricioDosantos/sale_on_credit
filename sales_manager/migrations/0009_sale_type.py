# Generated by Django 4.1 on 2022-08-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0008_alter_sale_div_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('Saída', 'Saída'), ('Entrada', 'Entrada')], default='Saída', max_length=20),
        ),
    ]
