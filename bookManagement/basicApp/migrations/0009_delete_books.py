# Generated by Django 4.0.2 on 2022-05-11 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0008_delete_issuedbooks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
    ]
