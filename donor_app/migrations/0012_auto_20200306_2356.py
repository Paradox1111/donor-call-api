# Generated by Django 3.0.4 on 2020-03-06 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donor_app', '0011_auto_20200306_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='steward',
        ),
        migrations.AddField(
            model_name='donor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='donors', to=settings.AUTH_USER_MODEL),
        ),
    ]
