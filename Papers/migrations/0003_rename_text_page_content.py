# Generated by Django 4.1 on 2022-08-09 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Papers', '0002_page_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='text',
            new_name='content',
        ),
    ]
