# Generated by Django 4.2.3 on 2023-07-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
