from django.urls import path
from main.views import index, signup, login, logout

urlpatterns = [
    path("", index, name="index"),
    path("index", index, name="index"),
    path("signup", signup, name="signup"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
]
