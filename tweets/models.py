from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

from .validators import validate_content
# Create your models here.

# We can also write our own validation function

'''
def validate_content(value):
    content = value
    if content == "shit" or content == "SHIT" or content == "Shit":
        raise ValidationError("Watch your language!")
    return value
'''


class Tweet(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    content = models.CharField(max_length=199, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def clean(self, *args, **kwargs):
        content = self.content
        if content == "fuck" or content == "Fuck" or content == "FUCK":
            raise ValidationError("Cannot be rude!")
        return super(Tweet, self).clean(*args, **kwargs)
