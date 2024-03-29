# Generated by Django 5.0.2 on 2024-03-07 12:45

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_texdraft_finalized_alter_draftfield_jinja_variable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='texdraft',
            name='tex_draft_preview',
            field=models.FileField(blank=True, null=True, upload_to=main.models.file_upload_path),
        ),
        migrations.AlterField(
            model_name='texdraft',
            name='tex_draft_file',
            field=models.FileField(upload_to=main.models.file_upload_path),
        ),
    ]
