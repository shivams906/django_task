from django.urls import path
from .views import UserCreate, UserDetail, UserUpdate

urlpatterns = [
    path("", UserCreate.as_view(), name="list_or_create"),
    path("profile/", UserDetail.as_view(), name="profile"),
    path("profile/edit/", UserUpdate.as_view(), name="edit_profile"),
]
