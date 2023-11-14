from django.views.generic import TemplateView
import logging

logger = logging.getLogger(__name__)


class LandingView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        logger.info('Landing page visited', extra={
            'user': str(request.user),
            'language': request.META.get('HTTP_ACCEPT_LANGUAGE'),
            'user_agent': request.META.get('HTTP_USER_AGENT')
        })
        return super().get(request, *args, **kwargs)
