from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    TweetListAPIView,
    TweetCreateAPIView,
    # TweetDetailView,
)

app_name = 'tweets-api'

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list'),
    path('create/', TweetCreateAPIView.as_view(), name='create'),
    #path('<int:pk>/', TweetDetailView().as_view(), name='detial'),
    # path('admin/', admin.site.urls),
]
