# Generated by Django 4.0.2 on 2022-02-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_profile_facebook_url_profile_insta_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='No Bio  Available', null=True),
        ),
    ]
