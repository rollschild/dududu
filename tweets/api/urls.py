from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    TweetListAPIView,
    TweetCreateAPIView,
    RetweetAPIView,
    LikeToggleAPIView,
)

app_name = 'tweets-api'

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list'),
    path('create/', TweetCreateAPIView.as_view(), name='create'),
    path(
        '<int:pk>/retweet/',
        RetweetAPIView.as_view(),
        name='retweet'),
    path('<int:pk>/like/', LikeToggleAPIView.as_view(), name='like-toggle'),
    # /api/tweet/id/retweet/
    # path('admin/', admin.site.urls),
]
