# Generated by Django 3.2.8 on 2021-10-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_dish_ifile'),
    ]

    operations = [
        migrations.CreateModel(
            name='waste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total', models.IntegerField()),
                ('wastage', models.IntegerField()),
            ],
        ),
    ]
