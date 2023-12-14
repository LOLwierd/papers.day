# Generated by Django 4.0.5 on 2023-06-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_category_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='short_name',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]
