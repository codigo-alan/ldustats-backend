# Generated by Django 4.2.1 on 2023-07-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_file_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='distance',
        ),
        migrations.AddField(
            model_name='session',
            name='accMin',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='accelerations',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='decMin',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='decelerations',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='drillTitle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='dtMin',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='hmlDistance',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='hsr',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='hsrMin',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='maxSpeed',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='spints',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='sprintDistance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='totalDistance',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='totalTime',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='zone4',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='zone5',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='zone6',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
