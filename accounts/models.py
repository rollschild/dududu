from django.db import models
from django.conf import settings
# Create your models here.


class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        queryset = self.get_queryset().all()
        try:
            if self.instance:
                queryset = queryset.exclude(user=self.instance)
        except BaseException:
            pass
        return queryset


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile', on_delete=models.CASCADE)
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='followed_by')

    objects = UserProfileManager()
    # equivalent to
    # UserProfileManager.objects.all()

    '''
    user.profile.following --- users I follow
    user.followed_by --- users that follow me
    some users might not have a profile, but still needs to show
    ...followed_by --- reverse relations
    '''

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)
