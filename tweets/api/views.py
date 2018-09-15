from rest_framework import generics
from django.db.models import Q
from tweets.models import Tweet
from .serializers import TweetModelSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import StandardResultsPagination


class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        tweet_queryset = Tweet.objects.filter(pk=pk)
        message = "Not allowed to retweet!"
        if tweet_queryset.exists() and tweet_queryset.count() == 1:
            if request.user.is_authenticated:
                new_tweet = Tweet.objects.retweet(
                    request.user, tweet_queryset.first())
                if new_tweet is not None:
                    data = TweetModelSerializer(new_tweet).data
                    return Response(data)
                message = "Retweet failed!!!"
        return Response({"message": message}, 400)


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")
        if requested_user:
            queryset = Tweet.objects.filter(
                user__username=requested_user).order_by("-timestamp")
        else:
            my_followings = self.request.user.profile.get_following()
            queryset_others = Tweet.objects.filter(
                user__in=my_followings)
            queryset_mine = Tweet.objects.filter(user=self.request.user)
            queryset = (
                queryset_others | queryset_mine).distinct().order_by("-timestamp")
            # or... orderby("-pk")
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(Q(content__icontains=query)
                                       | Q(user__username__icontains=query))
        return queryset
