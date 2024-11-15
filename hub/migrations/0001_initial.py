# Generated by Django 5.1.3 on 2024-11-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artname', models.TextField(max_length=100)),
                ('Arttype', models.TextField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Artid', models.IntegerField()),
            ],
        ),
    ]