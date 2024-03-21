import base64

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseServerError, HttpResponseBadRequest, FileResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

import requests
from requests.exceptions import ConnectionError

from createx.settings import TEX_ENGINE_URL
from main.forms import SearchForm, DraftFieldFillForm
from main.jinja_pdf_utils import text_is_tex_draft
from main.mixins import OwnerAccessMixin
from main.models import TexDraft, DraftField


class TexDraftListView(ListView):
    model = TexDraft
    paginate_by = 16
    template_name = 'tex_draft/list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = self.model.objects.filter(Q(is_public=True) | Q(owner=self.request.user))
            show_user_created = self.request.GET.get('show_user_tex_drafts', 'off')
            if show_user_created == 'on':
                queryset = queryset.filter(owner=self.request.user)
        else:
            queryset = self.model.objects.filter(is_public=True)

        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search_query')
        context['show_user_tex_drafts'] = self.request.GET.get('show_user_tex_drafts', 'off')
        context['search_form'] = SearchForm(self.request.GET)
        return context


class TexDraftDetailView(DetailView):
    model = TexDraft
    template_name = 'tex_draft/detail.html'
    context_object_name = 'tex_draft'


class TexDraftCreateView(LoginRequiredMixin, CreateView):
    model = TexDraft
    template_name = 'tex_draft/create.html'
    fields = ['name', 'description', 'is_public', 'is_restricted', 'tex_draft_file']
    success_url = reverse_lazy('tex_draft_list')

    def form_valid(self, form):
        if form.instance.tex_draft_file:
            file_contents = form.instance.tex_draft_file.open('r').read()
            if not text_is_tex_draft(file_contents):
                messages.warning(request=self.request, message='Tex draft should have at leas one draft_field to fill')
                return self.form_invalid(form)
        else:
            form.instance.tex_draft_file = 'example.tex'
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('fields_create', kwargs={'tex_draft_uuid': self.object.uuid})


class TexDraftUpdateView(LoginRequiredMixin, OwnerAccessMixin, UpdateView):
    model = TexDraft

    template_name = 'tex_draft/update.html'
    fields = ['name', 'description', 'is_public', 'is_restricted']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs) | {'tex_draft': self.object}


class TexDraftDeleteView(LoginRequiredMixin, OwnerAccessMixin, SuccessMessageMixin, DeleteView):
    model = TexDraft
    template_name = 'tex_draft/delete.html'
    success_message = 'Deleted!'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tex_draft_list')


class TexDraftFillView(FormView):
    template_name = 'tex_draft/fill.html'
    form_class = DraftFieldFillForm
    @property
    def tex_draft(self):
        return TexDraft.objects.get(uuid=self.kwargs['pk'])

    def get_form_kwargs(self):
        return super().get_form_kwargs() | {
            'draft_fields': DraftField.objects.filter(tex_draft=self.tex_draft)
        }

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {
            'tex_draft_name': self.tex_draft.name,
            'tex_draft_pk': self.tex_draft.pk
        }


class GetPDFView(View):

    @property
    def tex_draft(self):
        return TexDraft.objects.get(uuid=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy('tex_draft_fill', kwargs={'pk': self.tex_draft.pk}))

    def post(self, request, *args, **kwargs):
        form_data = request.POST.dict()
        form_data.pop('csrfmiddlewaretoken')
        with open(self.tex_draft.tex_draft_file.path, 'r') as tex_draft:
            tex_draft_data = tex_draft.read()
        json_data = {
            'template': tex_draft_data,
            'variables': form_data
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/pdf',
        }
        try:
            response = requests.post(TEX_ENGINE_URL, json=json_data, headers=headers)
        except ConnectionError:
            return HttpResponseServerError('Sorry! Can\'t access the pdf generating service. Try again later')
        if response.status_code == 200:
            base64_pdf_data = base64.b64encode(response.content).decode()
            return render(self.request, template_name='components/pdf_display.html', context={'pdf_data': base64_pdf_data})
        return HttpResponseBadRequest(f'An error occurred: {response.json()["message"]}')


class TexDraftPreviewView(View):
    def get(self, request, *args, **kwargs):
        return FileResponse(TexDraft.objects.get(pk=self.kwargs['pk']).preview, headers={'X-Frame-Options': 'SAMEORIGIN'})


class TexDraftFirstPageView(View):
    def get(self, request, *args, **kwargs):
        return FileResponse(TexDraft.objects.get(pk=self.kwargs['pk']).first_page, headers={'X-Frame-Options': 'SAMEORIGIN'})
