# Generated by Django 2.1 on 2018-09-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_tweet_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='reply',
            field=models.BooleanField(default=False, verbose_name='Is a reply?'),
        ),
    ]
