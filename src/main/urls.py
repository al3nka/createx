from django.urls import path
from main.views.general import LandingView
from main.views.account import ProfileDetailView, CustomLoginView
from main.views.tex_draft import TexDraftListView, TexDraftCreateView, TexDraftDetailView, TexDraftUpdateView, \
    TexDraftDeleteView, TexDraftFillView, GetPDFView
from main.views.draft_field import DraftFieldCreateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', LandingView.as_view(), name='index'),
    path('account/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('account/login/', CustomLoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),

    path('tex_drafts/', TexDraftListView.as_view(), name='tex_draft_list'),
    path('tex_drafts/create/', TexDraftCreateView.as_view(), name='tex_draft_create'),
    path('tex_drafts/<str:pk>/', TexDraftDetailView.as_view(), name='tex_draft_detail'),
    path('tex_drafts/edit/<str:pk>/', TexDraftUpdateView.as_view(), name='tex_draft_update'),
    path('tex_drafts/delete/<str:pk>/', TexDraftDeleteView.as_view(), name='tex_draft_delete'),

    path('tex_drafts/<str:tex_draft_uuid>/fields/create/', DraftFieldCreateView.as_view(), name='fields_create'),

    path('tex_drafts/<str:pk>/fill', TexDraftFillView.as_view(), name='tex_draft_fill'),

    path('tex_drafts/<str:pk>/pdf', GetPDFView.as_view(), name='pdf_generate'),
]
