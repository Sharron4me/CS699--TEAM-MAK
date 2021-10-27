# Generated by Django 3.2.8 on 2021-10-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_waste'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('text', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('ifile', models.ImageField(default='', upload_to='static/assets')),
            ],
        ),
    ]