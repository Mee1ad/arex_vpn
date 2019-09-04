from django.urls import path
from server.views import *

app_name = 'server'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('ping', Ping.as_view(), name='ping'),
]
