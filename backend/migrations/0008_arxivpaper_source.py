# Generated by Django 4.0.5 on 2023-06-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_arxivpaper_comment_arxivpaper_doi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arxivpaper',
            name='source',
            field=models.FileField(blank=True, null=True, upload_to='sources'),
        ),
    ]
