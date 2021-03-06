# Generated by Django 3.2.5 on 2021-07-26 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adresse', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Objet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiving_date', models.DateTimeField(auto_now_add=True)),
                ('giving_date', models.DateTimeField(verbose_name='date published')),
                ('type', models.CharField(max_length=200)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur')),
            ],
        ),
    ]
