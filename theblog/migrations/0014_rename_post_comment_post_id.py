# Generated by Django 4.0.2 on 2022-02-21 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_comment_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
    ]
