# Generated by Django 2.2.6 on 2019-11-04 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191103_1646'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]