# Generated by Django 3.0.3 on 2021-02-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20210222_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
    ]
