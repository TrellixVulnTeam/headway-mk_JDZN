# Generated by Django 3.0.7 on 2021-02-06 20:24

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0010_auto_20210206_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='banner_overlay',
            field=wagtail_color_panel.fields.ColorField(blank=True, help_text='Select color of banner overlay', max_length=7, null=True, verbose_name='Banner Overlay Color'),
        ),
    ]
