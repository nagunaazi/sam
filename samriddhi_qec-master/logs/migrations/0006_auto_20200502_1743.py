# Generated by Django 2.1.5 on 2020-05-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_paymentlog_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentlog',
            name='Payment_Request',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='paymentlog',
            name='Payment_Response',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
