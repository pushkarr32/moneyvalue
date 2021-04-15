# Generated by Django 3.1.6 on 2021-03-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_emailrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=300)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
