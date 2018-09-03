from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import get_user_model


# Create your views here.

User = get_user_model()


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    # *auth* is the actual app that user is associated to
    # ...and model is user
    queryset = User.objects.all()
    # slug_field = "username"
    '''
    def get_slug_field(self):
        return "username"
    '''

    def get_object(self):
        return get_object_or_404(
            User, username__iexact=self.kwargs.get("username"))
