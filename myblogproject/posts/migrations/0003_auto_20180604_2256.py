# Generated by Django 2.0.5 on 2018-06-04 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180604_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='title',
        ),
    ]
