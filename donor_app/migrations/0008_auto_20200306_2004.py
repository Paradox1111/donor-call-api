# Generated by Django 3.0.4 on 2020-03-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor_app', '0007_auto_20200306_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='orgname',
            new_name='orgName',
        ),
    ]
