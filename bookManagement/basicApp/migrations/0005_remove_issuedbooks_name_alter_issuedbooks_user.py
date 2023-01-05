# Generated by Django 4.0.2 on 2022-03-06 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicApp', '0004_issuedbooks_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbooks',
            name='name',
        ),
        migrations.AlterField(
            model_name='issuedbooks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
