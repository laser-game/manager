from django.contrib.auth import views as auth_views
from django.urls import path

from .apps import WebConfig
from .views import index


app_name = WebConfig.name
urlpatterns = [
    # first has higher priority
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('settings', index.settings, name='settings'),
    path('stream', index.stream, name='stream'),
    path('archive', index.archive, name='archive'),
    path('', index.index, name='index'),
]
