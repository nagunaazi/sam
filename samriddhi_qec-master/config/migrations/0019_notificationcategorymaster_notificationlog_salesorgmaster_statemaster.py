# Generated by Django 2.2.8 on 2020-08-04 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0018_tockenuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationCategoryMaster',
            fields=[
                ('NotiCat_Id', models.AutoField(primary_key=True, serialize=False)),
                ('NotiCat_Text', models.CharField(max_length=50, unique=True)),
                ('NotiCat_Screen', models.CharField(default='Dashboard', max_length=50)),
                ('status', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'NotificationCategoryMaster',
            },
        ),
        migrations.CreateModel(
            name='SalesOrgMaster',
            fields=[
                ('SalesOrg_Id', models.AutoField(primary_key=True, serialize=False)),
                ('State_Code', models.TextField(max_length=50)),
                ('SalesOrg_Code', models.TextField(max_length=50)),
                ('SalesOrg_Text', models.TextField(blank=True, max_length=250, null=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'SalesOrgMaster',
            },
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('State_Id', models.AutoField(primary_key=True, serialize=False)),
                ('State_Code', models.TextField(max_length=50)),
                ('State_Text', models.TextField(max_length=250)),
                ('State_Leng', models.TextField(default='EN', max_length=50)),
                ('status', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'StateMaster',
            },
        ),
        migrations.CreateModel(
            name='NotificationLog',
            fields=[
                ('Nitification_Id', models.AutoField(primary_key=True, serialize=False)),
                ('State', models.TextField(blank=True, max_length=50, null=True)),
                ('Notification_Leng', models.TextField(blank=True, default='EN', max_length=50, null=True)),
                ('SalseOrg', models.TextField(blank=True, max_length=50, null=True)),
                ('BP_Code', models.TextField(blank=True, max_length=30, null=True)),
                ('Notification_Title', models.TextField(blank=True, max_length=255, null=True)),
                
                ('Notification_To', models.TextField(blank=True, max_length=5000, null=True)),
                ('Notification_body', models.TextField(blank=True, max_length=5000, null=True)),
                ('Sent_Status', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Sent_On', models.DateTimeField(blank=True, null=True)),
                ('Read_Status', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Read_On', models.DateTimeField(blank=True, null=True)),
                ('googleapis_Response_Code', models.TextField(blank=True, max_length=50, null=True)),
                ('googleapis_Response_Body', models.TextField(blank=True, max_length=5000, null=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('usermaster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'NotificationLog',
            },
        ),
    ]
