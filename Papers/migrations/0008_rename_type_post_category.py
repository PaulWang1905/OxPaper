# Generated by Django 4.1 on 2022-08-09 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Papers', '0007_post_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='type',
            new_name='category',
        ),
    ]
