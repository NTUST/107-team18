from django.conf.urls import url
from . import views

urlpatterns = [
    # users
    url(r'^$', views.users_panel, name='users_panel'),
]