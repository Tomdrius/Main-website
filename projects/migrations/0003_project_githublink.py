# Generated by Django 5.0.2 on 2024-02-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githublink',
            field=models.CharField(default='empty link', max_length=40),
            preserve_default=False,
        ),
    ]
