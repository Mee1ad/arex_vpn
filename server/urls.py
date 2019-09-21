from django.urls import path
from server.views import *
from server.form import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'server'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('send_form', Form.as_view(), name='send_form'),
    # path('form', TemplateView.as_view(template_name='form.html')),
    path('form', FormView.as_view(), name='form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
