# Generated by Django 4.2.6 on 2023-12-05 13:06

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_texdraft_tex_draft_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texdraft',
            name='tex_draft_file',
            field=models.FileField(blank=True, null=True, upload_to=main.models.file_upload_path),
        ),
    ]