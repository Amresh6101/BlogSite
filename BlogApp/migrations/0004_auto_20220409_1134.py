# Generated by Django 3.2.10 on 2022-04-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_auto_20220409_0933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
