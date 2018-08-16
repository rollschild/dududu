from django.urls import path
from .views import (tweet_detail_view, tweet_list_view, TweetListView, TweetDetailView, TweetCreateView)

urlpatterns = [
    path('', TweetListView.as_view(), name="list"),
    path('<int:pk>/', TweetDetailView.as_view(), name="detail"),
    path('create/', TweetCreateView.as_view(), name='create'),
    # path('admin/', admin.site.urls),
]
