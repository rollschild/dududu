# Generated by Django 2.1 on 2018-09-03 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20180902_0302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp', 'content']},
        ),
    ]
