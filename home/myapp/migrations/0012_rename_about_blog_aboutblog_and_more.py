# Generated by Django 4.2.11 on 2024-05-22 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_adress_personal_info_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About_Blog',
            new_name='AboutBlog',
        ),
        migrations.RenameModel(
            old_name='Title_about',
            new_name='TitleAbout',
        ),
    ]