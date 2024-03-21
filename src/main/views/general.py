from django.views.generic import TemplateView
import logging

from main.models import TexDraft, UserRecentTexDrafts

logger = logging.getLogger(__name__)


class LandingView(TemplateView):

    @property
    def user(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        logger.info('Landing page visited', extra={
            'user': str(request.user),
            'language': request.META.get('HTTP_ACCEPT_LANGUAGE'),
            'user_agent': request.META.get('HTTP_USER_AGENT')
        })
        return super().get(request, *args, **kwargs)

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return 'user_welcome.html'
        else:
            return 'index.html'

    def get_context_data(self, **kwargs):
        context = {}
        if self.user.is_authenticated:
            context['tex_drafts'] = self.get_user_tex_drafts()
            context['recent_tex_drafts'] = UserRecentTexDrafts.objects.filter(user=self.user)
        return super().get_context_data() | context

    def get_user_tex_drafts(self):
        return TexDraft.objects.filter(owner=self.user)

