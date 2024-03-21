from django.contrib import admin
from main.models import TexDraft, DraftField, RegistrationInvitation, UserRecentTexDrafts

admin.site.register(TexDraft)
admin.site.register(DraftField)
admin.site.register(RegistrationInvitation)
admin.site.register(UserRecentTexDrafts)
