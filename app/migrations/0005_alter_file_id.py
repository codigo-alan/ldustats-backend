# Generated by Django 4.2.1 on 2023-07-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_file_session_idplayer_alter_player_id_session_idfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]