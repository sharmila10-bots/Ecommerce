# Generated by Django 3.1.3 on 2020-12-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discountedprice', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=70)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
