# Generated by Django 5.0.2 on 2024-03-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_texdraft_tex_draft_first_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texdraft',
            old_name='tex_draft_first_page',
            new_name='first_page',
        ),
        migrations.RenameField(
            model_name='texdraft',
            old_name='tex_draft_preview',
            new_name='preview',
        ),
    ]
