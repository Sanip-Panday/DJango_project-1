# Generated by Django 5.0.6 on 2024-05-28 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_aboutblog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutblog',
            old_name='blog_title',
            new_name='name',
        ),
    ]