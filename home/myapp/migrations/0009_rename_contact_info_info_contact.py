# Generated by Django 4.2.11 on 2024-05-22 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_title_contact_contact_info'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_info',
            new_name='info_contact',
        ),
    ]