# Generated by Django 3.1.6 on 2021-05-29 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]
