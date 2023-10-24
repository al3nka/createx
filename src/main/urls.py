from django.urls import path
from main.views.general import IndexView
from main.views.profile import ProfileDetailView
from main.views.tex_draft import TexDraftListView, TexDraftCreateView, TexDraftDetailView, TexDraftUpdateView, \
    TexDraftDeleteView
from main.views.draft_field import DraftFieldCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user/<int:pk>/', ProfileDetailView.as_view(), name='profile'),

    path('tex_drafts/', TexDraftListView.as_view(), name='templates_list'),
    path('tex_drafts/create/', TexDraftCreateView.as_view(), name='template_create'),
    path('tex_drafts/<str:pk>/', TexDraftDetailView.as_view(), name='template_detail'),
    path('tex_drafts/edit/<str:pk>/', TexDraftUpdateView.as_view(), name='template_update'),
    path('tex_drafts/delete/<str:pk>/', TexDraftDeleteView.as_view(), name='template_delete'),
    path('tex_drafts/fill/<str:pk>/', TexDraftUpdateView.as_view(), name='template_fill'),

    path('tex_drafts/<str:template_uuid>/fields/create/', DraftFieldCreateView.as_view(), name='fields_create'),
]
