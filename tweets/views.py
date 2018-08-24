from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView)
from django.forms.utils import ErrorList
from django import forms
from django.urls import reverse_lazy
from django.db.models import Q

from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TweetModelForm
from .models import Tweet

# Create


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = '/tweet/create/'
    # success_url = reverse_lazy('tweets:detail')

    # adjustable url
    login_url = '/admin/'
    # fields = ['user', 'content']

    '''
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(TweetCreateView, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ["User must be logged in to continue!!!"])
            return self.form_invalid(form)
    '''
# Function to create view


def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        "form": form
    }
    return render(request, 'tweets/create_view.html', context)

# Update view


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = "/tweet/"
    login_url = "/admin/"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweets:list")
    template_name = 'tweets/delete_confirm.html'


# List and retrieve


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = "tweets/detail_view.html"
    '''
    def get_object(self):
        print(self.kwargs)  # {'pk': something}
        pk = self.kwargs.get("pk")
        print(pk)  # None
        return Tweet.objects.get(id=pk)
    '''


class TweetListView(ListView):
    def get_queryset(self, *args, **kwargs):
        queryset = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(Q(content__icontains=query)
                                       | Q(user__username__icontains=query))
        return queryset
    # template_name = "tweets/list_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["create_form"] = TweetModelForm()
        context["create_url"] = reverse_lazy("tweets:create")
        return context


def tweet_detail_view(request, pk=None):
    # obj = Tweet.objects.get(id=pk)
    obj = get_object_or_404(Tweet, id=pk)
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
