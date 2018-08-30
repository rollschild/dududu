from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
from .models import Tweet

User = get_user_model()


class TweetModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='rollschild')

    def test_tweet_post(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='It\'s a test tweet.'
        )
        self.assertTrue(obj.content == 'It\'s a test tweet.')
        self.assertTrue(obj.id == 1)
        absolute_url = reverse('tweets:detail', kwargs={'pk': 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='Test urls.'
        )
        absolute_url = reverse('tweets:detail', kwargs={'pk': obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
