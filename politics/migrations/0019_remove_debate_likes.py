# Generated by Django 2.1.2 on 2019-03-18 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0018_auto_20190318_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debate',
            name='likes',
        ),
    ]
