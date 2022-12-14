# Generated by Django 4.1 on 2022-08-09 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Papers', '0003_rename_text_page_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-date_added'], 'verbose_name_plural': 'pages'},
        ),
        migrations.AddField(
            model_name='page',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
