# Generated by Django 3.1.3 on 2021-08-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baan_id', models.CharField(max_length=50, unique=True)),
                ('item_name', models.CharField(blank=True, max_length=50)),
                ('screw_thread', models.CharField(max_length=5)),
                ('diameter', models.DecimalField(decimal_places=2, max_digits=3)),
                ('length', models.DecimalField(decimal_places=2, max_digits=4)),
                ('strength', models.DecimalField(blank=True, decimal_places=1, max_digits=2)),
                ('iso', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=10)),
                ('assembly_place', models.CharField(max_length=10, unique=True)),
                ('warehouse_place', models.CharField(max_length=10)),
                ('file', models.FileField(blank=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Винт',
                'verbose_name_plural': 'Винты',
            },
        ),
    ]