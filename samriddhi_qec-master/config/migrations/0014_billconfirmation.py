# Generated by Django 2.0.2 on 2020-06-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0013_banktransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillConfirmation',
            fields=[
                ('BillConfirmation_id', models.AutoField(primary_key=True, serialize=False)),
                ('Bill_Period', models.CharField(blank=True, max_length=30, null=True)),
                ('Bill_No', models.CharField(blank=True, max_length=30, null=True)),
                ('BP_Code', models.CharField(blank=True, max_length=30, null=True)),
                ('Confirm_Status', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('Confirm_Remark', models.TextField(blank=True, max_length=255, null=True)),
                ('Confirm_By', models.CharField(blank=True, max_length=30, null=True)),
                ('Confirm_On', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'BillConfirmation',
            },
        ),
    ]
