from django.db import models
from django.urls import reverse_lazy
# Create your models here.
from tweets.models import Tweet
from .signals import parsed_hashtags


class HashTag(models.Model):
    tag = models.CharField(max_length=139)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse_lazy("hashtag", kwargs={"hashtag": self.tag})

    def get_tweets(self):
        # directly related to the instance itself
        return Tweet.objects.filter(content__icontains="#" + self.tag)


def parsed_hashtags_receiver(sender, hashtag_list, *args, **kwargs):
    if len(hashtag_list) > 0:
        for tag in hashtag_list:
            new_tag, create = HashTag.objects.get_or_create(tag=tag)


parsed_hashtags.connect(parsed_hashtags_receiver)
