"""dududu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from .views import index
from tweets.views import TweetListView
from hashtags.views import HashTagView

urlpatterns = [
    path('', TweetListView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('tags/<path:hashtag>/', HashTagView.as_view(), name="hashtag"),
    # path('profiles/', include('accounts.urls', namespace='profiles')),
    path('tweet/', include('tweets.urls', namespace='tweets')),
    path('api/tweet/', include('tweets.api.urls', namespace='tweets-api')),
    path('api/', include('accounts.api.urls', namespace='profiles-api')),
    path('', include('accounts.urls', namespace='profiles')),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
