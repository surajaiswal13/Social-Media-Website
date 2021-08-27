from django.shortcuts import render
from . import forms
from accounts.models import User
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from groups.models import Group
# from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

class Search(ListView):
    model = Group
    template_name = "accounts/search.html"

    def get_queryset(self):
        search_input = self.request.GET["query"]
        return Group.objects.filter(Q(name__icontains=search_input)|Q(description__icontains=search_input))
        # return Group.objects.all()
