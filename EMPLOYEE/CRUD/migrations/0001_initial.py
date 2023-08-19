# Generated by Django 4.1.4 on 2023-08-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('skill', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=15)),
            ],
        ),
    ]
