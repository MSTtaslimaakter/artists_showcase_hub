# Generated by Django 4.2.16 on 2024-11-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_market_place_delete_event_s'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('organizer', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Market_place',
        ),
    ]
