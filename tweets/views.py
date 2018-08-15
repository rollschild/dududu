from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tweet
# List and retrieve


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = "tweets/detail_view.html"

    def get_object(self):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    # template_name = "tweets/list_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self). get_context_data(*args, **kwargs)
        return context


def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    print(obj.content)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
