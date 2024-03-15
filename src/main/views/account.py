from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import translation

from django.http import Http404
from django.views import View
from django.views.generic import DetailView, RedirectView, CreateView

from createx.settings import LANGUAGE_COOKIE_NAME, LOGOUT_REDIRECT_URL
from main.models import user_model, RegistrationInvitation


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


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(LOGOUT_REDIRECT_URL)


class RegisterView(CreateView):
    model = user_model
    template_name = 'account/register.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('index')

    @property
    def registration_invitation(self):
        return RegistrationInvitation.objects.get(invitation_code=self.kwargs['invitation_code'])

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        print(request.COOKIES.get(LANGUAGE_COOKIE_NAME))
        if not request.COOKIES.get(LANGUAGE_COOKIE_NAME):
            translation.activate(self.registration_invitation.user_lang)
            response.set_cookie(LANGUAGE_COOKIE_NAME, self.registration_invitation.user_lang)
        return response

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs) | {'users_name': self.registration_invitation.user_name}

    def form_valid(self, form):
        self.registration_invitation.delete()
        return super().form_valid(form)
