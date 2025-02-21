# Generated by Django 4.2 on 2025-02-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognom1', models.CharField(max_length=100)),
                ('cognom2', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('curs', models.CharField(max_length=100)),
                ('moduls', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('cognom1', models.CharField(max_length=100)),
                ('cognom2', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('curs', models.CharField(max_length=200)),
                ('tutor', models.CharField(max_length=2)),
                ('moduls', models.CharField(max_length=200)),
            ],
        ),
    ]
