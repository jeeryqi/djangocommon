from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class TestLogin(LoginRequiredMixin, generic.ListView):
    queryset = [1, 2, 3]
    template_name = 'testing/test_login.html'
