# Generated by Django 3.0.5 on 2020-05-13 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medical', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ambulance',
        ),
        migrations.DeleteModel(
            name='Genetic_disorder',
        ),
        migrations.DeleteModel(
            name='Medical_history',
        ),
        migrations.DeleteModel(
            name='Support',
        ),
    ]