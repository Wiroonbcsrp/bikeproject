# Generated by Django 2.0.4 on 2018-04-27 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bike_management', '0002_auto_20180427_0622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='book',
            name='detail',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]