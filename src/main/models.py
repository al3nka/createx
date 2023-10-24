import uuid as uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.contrib.auth.models import Group

user_model = get_user_model()


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
    tex_draft_file = models.FileField(upload_to='tex_drafts')
    owner = models.ForeignKey(to=user_model, on_delete=models.CASCADE, related_name='tex_drafts')

    def __str__(self):
        return f'TexDraft: "{self.name}"'

    def get_absolute_url(self):
        return reverse('tex_draft_detail', kwargs={'pk': str(self.pk)})


class DraftField(models.Model):
    name = models.CharField(max_length=50)
    help_text = models.CharField(blank=True, null=True)
    jinja_variable = models.CharField(max_length=255)
    tex_draft = models.ForeignKey(to=TexDraft, on_delete=models.CASCADE, related_name='fields')
    field_type = models.IntegerField(choices=DraftFieldType.choices)
