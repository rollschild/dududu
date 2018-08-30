from django.urls import path
from django.views.generic.base import RedirectView
from .views import (
    TweetListAPIView,
)

app_name = 'tweets-api'

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list')
    # path('admin/', admin.site.urls),
]
