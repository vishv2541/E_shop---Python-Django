# Generated by Django 5.0.1 on 2024-04-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0013_remove_order_amount_remove_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='', max_length=100, null='True'),
            preserve_default='True',
        ),
    ]
