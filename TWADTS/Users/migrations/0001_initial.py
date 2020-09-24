# Generated by Django 2.2.12 on 2020-06-12 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('Fname', models.CharField(max_length=500)),
                ('Lname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_Pic', models.ImageField(blank=True, upload_to='Profile_Pic')),
                ('Uname', models.CharField(max_length=50)),
                ('DOB', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Phone_no', models.IntegerField()),
                ('Add_line1', models.CharField(max_length=200)),
                ('Add_line2', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Postal_Code', models.IntegerField()),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.SignUp')),
            ],
        ),
        migrations.CreateModel(
            name='Bike_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bike_Model_Name', models.CharField(max_length=50)),
                ('Bike_No', models.CharField(max_length=50)),
                ('Bike_Reg_No', models.CharField(max_length=50)),
                ('Licence_No', models.CharField(max_length=50)),
                ('Licence', models.FileField(upload_to='Licence')),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.SignUp')),
            ],
        ),
    ]