# Generated by Django 2.1 on 2018-08-15 23:58

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20180814_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=199, validators=[tweets.models.validate_content]),
        ),
    ]
