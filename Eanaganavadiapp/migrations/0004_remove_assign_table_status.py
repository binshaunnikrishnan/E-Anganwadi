# Generated by Django 3.2.20 on 2023-11-08 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eanaganavadiapp', '0003_auto_20231106_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assign_table',
            name='status',
        ),
    ]