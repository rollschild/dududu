from django.core.exceptions import ValidationError
from django.db import models


def validate_content(value):
    content = value
    if content == "shit" or content == "SHIT" or content == "Shit":
        raise ValidationError("Watch your language!")
    return value
