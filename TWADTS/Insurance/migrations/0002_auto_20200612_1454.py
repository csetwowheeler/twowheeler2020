# Generated by Django 2.2.12 on 2020-06-12 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='user',
            new_name='email',
        ),
    ]