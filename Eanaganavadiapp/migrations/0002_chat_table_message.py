# Generated by Django 3.2.20 on 2023-11-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eanaganavadiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_table',
            name='message',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]