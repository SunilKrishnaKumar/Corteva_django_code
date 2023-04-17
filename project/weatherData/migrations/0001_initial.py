# Generated by Django 4.2 on 2023-04-16 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('max_temp', models.IntegerField(null=True)),
                ('min_temp', models.IntegerField(null=True)),
                ('precipitation', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=255)),
                ('avg_max_temp', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('avg_min_temp', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('total_precipitation', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
