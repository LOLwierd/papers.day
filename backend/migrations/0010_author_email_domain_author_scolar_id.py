# Generated by Django 4.0.5 on 2023-06-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_arxivpaper_source_arxivpaper_source_tar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email_domain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='scolar_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
