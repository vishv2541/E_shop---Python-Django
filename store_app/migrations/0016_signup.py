# Generated by Django 5.0.1 on 2024-04-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0015_order_amount_orderitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('passwd', models.CharField(max_length=15)),
                ('confpasswd', models.CharField(max_length=15)),
            ],
        ),
    ]
