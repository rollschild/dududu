from django.urls import path

from .views import (
    UserDetailView
)

app_name = "profiles"

urlpatterns = [
    path('<slug:username>/', UserDetailView.as_view(), name="detail"),
]
