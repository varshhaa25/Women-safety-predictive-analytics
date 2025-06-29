# Generated by Django 5.1.7 on 2025-03-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('Neighbourhood', models.CharField(max_length=255)),
                ('occurrencehour', models.IntegerField()),
                ('occurrencedayofweek', models.CharField(max_length=20)),
                ('premisetype', models.CharField(max_length=255)),
                ('crime_type', models.CharField(max_length=255)),
                ('crime_rate', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
