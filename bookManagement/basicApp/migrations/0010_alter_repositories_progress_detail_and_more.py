# Generated by Django 4.0.2 on 2022-05-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0009_delete_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositories',
            name='progress_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repositories',
            name='progress_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repositories',
            name='progress_video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
