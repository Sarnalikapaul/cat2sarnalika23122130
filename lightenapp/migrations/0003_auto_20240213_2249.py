# Generated by Django 3.0.5 on 2024-02-13 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightenapp', '0002_auto_20240213_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='UserProfile',
        ),
    ]
