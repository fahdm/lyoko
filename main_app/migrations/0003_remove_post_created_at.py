# Generated by Django 4.2.11 on 2024-04-30 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_post_title_tag_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]
