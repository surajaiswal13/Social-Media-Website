# Generated by Django 3.0.3 on 2020-08-31 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200901_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, upload_to='post_videos'),
        ),
    ]
