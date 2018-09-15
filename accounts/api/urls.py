from django.urls import path

from django.views.generic.base import RedirectView

from tweets.api.views import (TweetListAPIView)

app_name = "profiles-api"

urlpatterns = [
    path('<slug:username>/tweet/', TweetListAPIView.as_view(), name='list')
]
