from rest_framework import generics
from django.db.models import Q
from tweets.models import Tweet
from .serializers import TweetModelSerializer
from rest_framework import permissions
from .pagination import StandardResultsPagination


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
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
