# Generated by Django 4.1.7 on 2023-03-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('password', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]