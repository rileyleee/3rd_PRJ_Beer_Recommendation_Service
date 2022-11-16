# Generated by Django 4.1.3 on 2022-11-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image",
        ),
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="user_path/%Y/%m/%d"
            ),
        ),
    ]
