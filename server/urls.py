from django.urls import path
from server.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'server'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
