# Generated by Django 3.1.3 on 2021-08-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0003_auto_20210811_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='screw',
            name='place_line',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
