# Generated by Django 4.2b1 on 2023-07-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='viewcnt',
            field=models.IntegerField(default=0),
        ),
    ]