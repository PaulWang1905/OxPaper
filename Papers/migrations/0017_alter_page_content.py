# Generated by Django 4.1 on 2022-08-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Papers', '0016_page_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(),
        ),
    ]
