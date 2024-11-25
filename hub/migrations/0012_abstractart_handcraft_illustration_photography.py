# Generated by Django 4.2.16 on 2024-11-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0011_painting'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='abstract_arts/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HandCraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='hand_crafts/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Illustration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='illustrations/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='photography/')),
                ('description', models.TextField()),
            ],
        ),
    ]