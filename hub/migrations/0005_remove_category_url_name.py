# Generated by Django 4.2.16 on 2024-11-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_category_url_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url_name',
        ),
    ]
