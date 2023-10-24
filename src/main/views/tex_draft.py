from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.forms import SearchForm
from main.jinja_pdf_utils import text_is_tex_draft
from main.mixins import OwnerAccessMixin
from main.models import TexDraft


class TexDraftListView(LoginRequiredMixin, ListView):
    model = TexDraft
    paginate_by = 16
    template_name = 'tex_draft/list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(is_public=True)

        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            queryset = queryset.filter(name__icontains=search_query)

        show_user_created = self.request.GET.get('show_user_templates', 'off')
        if show_user_created == 'on':
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search_query')
        context['show_user_templates'] = self.request.GET.get('show_user_templates', 'off')
        context['search_form'] = SearchForm(self.request.GET)
        print(context)
        return context


class TexDraftDetailView(LoginRequiredMixin, DetailView):
    model = TexDraft
    template_name = 'tex_draft/detail.html'
    context_object_name = 'tex_draft'


class TexDraftCreateView(LoginRequiredMixin, CreateView):
    model = TexDraft
    template_name = 'tex_draft/create.html'
    fields = ['name', 'description', 'is_public', 'is_restricted', 'tex_draft_file']

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        file_contents = form.instance.tex_draft_file.open('r').read()
        if not text_is_tex_draft(file_contents):
            messages.warning(request=self.request, message="Template should have at leas one draft_field to fill")
            return self.form_invalid(form)
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fields_create', kwargs={'template_uuid': self.object.uuid})


class TexDraftUpdateView(LoginRequiredMixin, OwnerAccessMixin, UpdateView):
    model = TexDraft
    template_name = 'tex_draft/update.html'
    fields = ['name', 'description', 'is_public', 'is_restricted']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class TexDraftDeleteView(LoginRequiredMixin, OwnerAccessMixin, SuccessMessageMixin, DeleteView):
    model = TexDraft
    template_name = 'tex_draft/delete.html'
    success_message = 'Deleted!'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('templates_list')
