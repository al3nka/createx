from django.views.generic import CreateView

from main.models import DraftField


class DraftFieldCreateView(CreateView):
    model = DraftField