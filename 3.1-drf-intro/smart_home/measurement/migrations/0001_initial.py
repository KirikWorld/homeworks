# Generated by Django 4.0.3 on 2022-03-08 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('describe', models.CharField(blank=True, max_length=50, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик температуры',
                'verbose_name_plural': 'Датчики температуры',
            },
        ),
        migrations.CreateModel(
            name='Measurment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Температура')),
                ('date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата измерения')),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensors', verbose_name='ID датчика')),
            ],
            options={
                'verbose_name': 'Замер температуры',
                'verbose_name_plural': 'Замеры температуры',
            },
        ),
    ]
