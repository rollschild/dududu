from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    tweet_detail_view,
    tweet_list_view,
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView,
    RetweetView,
)

app_name = 'tweets'

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('search/', TweetListView.as_view(), name="list"),
    path('<int:pk>/', TweetDetailView.as_view(), name="detail"),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),
    path('<int:pk>/retweet/', RetweetView.as_view(), name='retweet'),
    # path('admin/', admin.site.urls),
]
