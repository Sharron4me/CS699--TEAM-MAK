# Generated by Django 3.2.8 on 2021-10-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='dns',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='campaign',
            name='status',
            field=models.CharField(default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='campaign',
            name='ups',
            field=models.CharField(default='', max_length=300),
        ),
    ]