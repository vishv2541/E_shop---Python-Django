# Generated by Django 5.0.1 on 2024-04-09 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0009_remove_order_addtional_information_remove_order_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]