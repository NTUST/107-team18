from django.urls import path

from users.views import users_panel

urlpatterns = [path("", users_panel, name="users_panel")]
