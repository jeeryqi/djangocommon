from django.urls import path
from django.views.generic.base import TemplateView
from .views import TestLogin

app_name = 'testing'
urlpatterns = [
    path('testlogin', TestLogin.as_view(), name='test_login'),
]
