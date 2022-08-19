# Generated by Django 4.1 on 2022-08-14 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dividend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('chip_id', models.CharField(max_length=200, unique=True)),
                ('limit', models.IntegerField()),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('purchase_date', models.DateField()),
                ('div_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_manager.dividend')),
            ],
        ),
    ]