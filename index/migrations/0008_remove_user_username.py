# Generated by Django 4.2b1 on 2023-07-25 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_user_managers_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
