# Generated by Django 3.0.7 on 2021-02-06 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210206_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_cta',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_subtitle',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
    ]
