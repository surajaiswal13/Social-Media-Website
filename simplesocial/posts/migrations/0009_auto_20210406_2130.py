# Generated by Django 3.0.3 on 2021-04-06 16:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210406_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
