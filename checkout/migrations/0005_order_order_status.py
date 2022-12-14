# Generated by Django 3.2 on 2022-12-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('SHIPPED', 'Shipped'), ('CANCELLED', 'Cancelled')], default='CONFIRMED', max_length=10),
        ),
    ]
