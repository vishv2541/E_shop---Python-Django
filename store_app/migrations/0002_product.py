# Generated by Django 5.0.1 on 2024-03-03 11:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(upload_to='Product_image/img')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(choices=[('new', 'new'), ('old', 'old')], max_length=100)),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stock', models.CharField(choices=[('in stock', 'in stock'), ('out of stock', 'out of stock')], max_length=100)),
                ('status', models.CharField(choices=[('publish', 'publish'), ('draft', 'draft')], max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.brand')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.categories')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.color')),
                ('filter_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.filter_price')),
            ],
        ),
    ]
