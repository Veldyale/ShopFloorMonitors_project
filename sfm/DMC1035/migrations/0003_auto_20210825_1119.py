# Generated by Django 3.2.5 on 2021-08-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMC1035', '0002_auto_20210811_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='circuit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
