# Generated by Django 5.0.2 on 2024-03-07 13:36

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_texdraft_tex_draft_preview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='texdraft',
            name='tex_draft_first_page',
            field=models.FileField(blank=True, null=True, upload_to=main.models.file_upload_path),
        ),
    ]
