# Generated by Django 4.2b1 on 2023-07-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60),
        ),
    ]