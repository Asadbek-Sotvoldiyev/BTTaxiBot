# Generated by Django 5.1.3 on 2024-11-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_ordertaxi_driver_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChatId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=100)),
                ('group_name', models.CharField(max_length=100)),
            ],
        ),
    ]
