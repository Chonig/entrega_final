# Generated by Django 4.0.5 on 2022-07-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=40)),
                ('calle', models.CharField(max_length=40)),
                ('altura', models.IntegerField()),
                ('cant_empleados', models.IntegerField()),
            ],
        ),
    ]
