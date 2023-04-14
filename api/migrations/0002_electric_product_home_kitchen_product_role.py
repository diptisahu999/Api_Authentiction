# Generated by Django 4.1.7 on 2023-03-03 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electric_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=23)),
                ('tv', models.CharField(max_length=23)),
                ('fan', models.CharField(max_length=23)),
            ],
            options={
                'db_table': 'ele_tbl',
            },
        ),
        migrations.CreateModel(
            name='Home_Kitchen_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
            ],
            options={
                'db_table': 'kit_product',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('created_role_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_role_date', models.DateTimeField(auto_now=True)),
                ('assigned_devices', models.ManyToManyField(blank=True, to='api.electric_product')),
            ],
            options={
                'db_table': 'role_tbl',
            },
        ),
    ]