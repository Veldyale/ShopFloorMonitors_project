# Generated by Django 3.1.3 on 2021-08-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_auto_20210811_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_A_first',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_A_second',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_B_first',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_B_second',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_C_first',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_C_second',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_D',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_H_first',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_H_second',
        ),
        migrations.RemoveField(
            model_name='screw',
            name='assembly_place_H_third',
        ),
        migrations.AddField(
            model_name='screw',
            name='assembly_place',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='screw',
            name='baan_id',
            field=models.CharField(max_length=50),
        ),
    ]
