# Generated by Django 3.2.5 on 2021-07-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210727_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='mdp',
            field=models.CharField(default='***', max_length=200),
        ),
    ]
