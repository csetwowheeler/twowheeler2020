# Generated by Django 3.0.5 on 2020-06-13 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='Email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.SignUp', unique=True),
        ),
    ]