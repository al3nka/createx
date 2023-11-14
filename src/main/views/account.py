from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.http import Http404
from django.views.generic import DetailView, RedirectView

from main.models import user_model


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = user_model
    template_name = 'account/detail.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if self.request.user == object:
            return object
        raise Http404()


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
