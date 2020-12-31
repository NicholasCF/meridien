# Generated by Django 3.0.7 on 2020-12-31 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_booking_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='amount_paid',
        ),
        migrations.AddField(
            model_name='booking',
            name='deposit_paid',
            field=models.BooleanField(default=False),
        ),
    ]
