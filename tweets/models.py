import re
from django.db.models.signals import post_save
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse

from .validators import validate_content
from hashtags.signals import parsed_hashtags
# Create your models here.


# We can also write our own validation function

'''
def validate_content(value):
    content = value
    if content == "shit" or content == "SHIT" or content == "Shit":
        raise ValidationError("Watch your language!")
    return value
'''


class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            original_parent = parent_obj.parent
        else:
            original_parent = parent_obj

        # Here we do NOT allow duplicate retweeting
        queryset = self.get_queryset().filter(user=user, parent=original_parent)
        if queryset.exists():
            return None

        obj = self.model(
            parent=parent_obj,
            user=user,
            content=parent_obj.content,
        )
        obj.save()
        return obj

    def like_toggle(self, user, tweet_obj):
        if user in tweet_obj.liked.all():
            user_liked = False
            tweet_obj.liked.remove(user)
        else:
            user_liked = True
            tweet_obj.liked.add(user)
        return user_liked


class Tweet(models.Model):
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    # When I tweet, it will create a copy of the original tweet
    # ...and give credit to the original tweet as well

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    content = models.CharField(max_length=140, validators=[validate_content])
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="liked")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.BooleanField(verbose_name="Is a reply?", default=False)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweets:detail", kwargs={"pk": self.pk})

    def clean(self, *args, **kwargs):
        content = self.content
        if content == "fuck" or content == "Fuck" or content == "FUCK":
            raise ValidationError("Cannot be rude!")
        return super(Tweet, self).clean(*args, **kwargs)

    class Meta:
        ordering = ['-timestamp', 'content']
        # NEED to do a migration if you do this


def tweet_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        # Notify the user
        user_regex = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regex, instance.content)
        # username = m.group("username")
        # print(username)
        # Send notification now!
        hash_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regex, instance.content)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)
        # hashtag = m.group("hashtag")
        # print(hashtag)


post_save.connect(tweet_save_receiver, sender=Tweet)
