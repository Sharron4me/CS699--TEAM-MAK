# Generated by Django 3.2.8 on 2021-10-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_admintable'),
    ]

    operations = [
        migrations.CreateModel(
            name='dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=100)),
                ('serve_time', models.CharField(max_length=50)),
            ],
        ),
    ]
