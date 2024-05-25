# Generated by Django 4.2.11 on 2024-05-22 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_title_about_about_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.title_contact')),
            ],
        ),
    ]