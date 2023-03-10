# Generated by Django 4.0.2 on 2022-05-11 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0011_commit'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commit',
            name='imageFile',
            field=models.URLField(blank=True),
        ),
    ]
