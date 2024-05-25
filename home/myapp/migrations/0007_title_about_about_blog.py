# Generated by Django 4.2.11 on 2024-05-22 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_email_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='About_Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('blog_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.title_about')),
            ],
        ),
    ]