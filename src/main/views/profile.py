from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView

from main.models import user_model


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = user_model
    template_name = 'user/detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if self.request.user == object:
            return object
        raise Http404()
