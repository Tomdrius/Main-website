# Generated by Django 5.0.2 on 2024-02-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_githublink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='githublink',
            field=models.SlugField(max_length=60),
        ),
    ]