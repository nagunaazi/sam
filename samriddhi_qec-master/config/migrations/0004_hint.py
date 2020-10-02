# Generated by Django 2.1.5 on 2020-04-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20200327_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('Hint_id', models.AutoField(primary_key=True, serialize=False)),
                ('Hint_Srno', models.IntegerField(blank=True, default=1, null=True)),
                ('Hint_Text', models.TextField(max_length=255)),
                ('Hint_Status', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
            ],
            options={
                'db_table': 'Hint',
            },
        ),
    ]
