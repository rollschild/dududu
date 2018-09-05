from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
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

    def toggle_follow(self, user, to_toggle_user):
        user_profile, created = UserProfile.objects.get_or_create(
            user=user)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            foed = False
        else:
            user_profile.following.add(to_toggle_user)
            foed = True
        return foed

    def is_following(self, user, user_followed_by_me):
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if user_followed_by_me in user_profile.following.all():
            return True
        return False


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

    def get_follow_url(self):
        return reverse_lazy("profiles:follow", kwargs={
                            "username": self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("profiles:detail", kwargs={
                            "username": self.user.username})
