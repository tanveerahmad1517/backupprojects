# Generated by Django 2.0.5 on 2018-06-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20180604_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='Post_images'),
        ),
    ]
