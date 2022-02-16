# Generated by Django 4.0.2 on 2022-02-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exist',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
