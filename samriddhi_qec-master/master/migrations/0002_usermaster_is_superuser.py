# Generated by Django 2.1.15 on 2020-03-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
