# Generated by Django 2.1.2 on 2019-03-14 15:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('politics', '0005_debate_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='comments',
        ),
        migrations.AddField(
            model_name='debate',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='likes',
        ),
    ]