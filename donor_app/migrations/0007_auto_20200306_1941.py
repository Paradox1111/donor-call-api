# Generated by Django 3.0.4 on 2020-03-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor_app', '0006_donor_botsteward'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='botSteward',
            new_name='botsteward',
        ),
        migrations.AlterField(
            model_name='donor',
            name='comments',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='lastgift',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='lastgiftdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='nextlastgift',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='nextlastgiftdate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='orgname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='paymentnum',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='yeartotal',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='steward',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='steward',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
