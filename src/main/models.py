import string
import uuid as uuid
import random
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.contrib.auth.models import Group
from django.utils.timezone import now

user_model = get_user_model()


def file_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/tex_drafts/<uuid>/<filename>
    return f"tex_drafts/{instance.uuid}/{filename}"


class DraftFieldType(models.IntegerChoices):
    NUMBER = 0, 'Number'
    TEXT = 1, 'Text'
    PARAGRAPH = 2, 'Paragraph'
    DATE = 3, 'Date'
    BOOL = 4, 'Boolean'


class TexDraft(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)  # if True, tex_draft will be displayed to everyone
    is_restricted = models.BooleanField(default=False)  # if True, tex_draft can be accessed by link
    tex_draft_file = models.FileField(upload_to=file_upload_path)
    owner = models.ForeignKey(to=user_model, on_delete=models.CASCADE, related_name='tex_drafts')
    finalized = models.BooleanField(default=False)

    preview = models.FileField(upload_to=file_upload_path, null=True, blank=True)
    first_page = models.FileField(upload_to=file_upload_path, null=True, blank=True)

    def __str__(self):
        return f'TexDraft: "{self.name}"'

    def get_absolute_url(self):
        return reverse('tex_draft_detail', kwargs={'pk': str(self.pk)})

    def view_tex_draft(self, user):
        user_recent_tex_drafts = UserRecentTexDrafts.objects.filter(user=user)
        try:
            recent_tex_draft = user_recent_tex_drafts.get(tex_draft=self)
            recent_tex_draft.date_viewed = now()
        except UserRecentTexDrafts.DoesNotExist:
            recent_tex_draft = UserRecentTexDrafts(user=user, tex_draft=self)
        recent_tex_draft.save()
        if len(user_recent_tex_drafts) > 5:
            user_recent_tex_drafts.last().delete()


class DraftField(models.Model):
    name = models.CharField(max_length=250)
    help_text = models.TextField(blank=True, null=True)
    jinja_variable = models.CharField(max_length=500)
    tex_draft = models.ForeignKey(to=TexDraft, on_delete=models.CASCADE, related_name='fields')
    field_type = models.IntegerField(choices=DraftFieldType.choices)


def generate_random_invitation_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))


class RegistrationInvitation(models.Model):
    invitation_code = models.CharField(default=generate_random_invitation_code, max_length=12, unique=True)
    user_name = models.CharField(blank=True, null=False, max_length=250)
    user_lang = models.CharField(max_length=2, default='en')

    def get_absolute_url(self):
        return reverse('registration', kwargs={'invitation_code': str(self.invitation_code)})


class UserRecentTexDrafts(models.Model):
    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE, related_name='recent_tex_drafts')
    tex_draft = models.ForeignKey(to=TexDraft, on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_viewed']
