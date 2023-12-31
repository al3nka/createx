# Generated by Django 4.2.6 on 2023-10-30 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TexDraft',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_restricted', models.BooleanField(default=False)),
                ('tex_draft_file', models.FileField(upload_to='tex_drafts')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tex_drafts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DraftField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('jinja_variable', models.CharField(max_length=255)),
                ('field_type', models.IntegerField(choices=[(0, 'Number'), (1, 'Text'), (2, 'Paragraph'), (3, 'Date'), (4, 'Boolean')])),
                ('tex_draft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='main.texdraft')),
            ],
        ),
    ]
