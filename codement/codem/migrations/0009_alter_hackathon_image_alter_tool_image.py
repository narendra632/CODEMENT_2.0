# Generated by Django 4.1.3 on 2023-11-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("codem", "0008_alter_channel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hackathon",
            name="image",
            field=models.ImageField(upload_to="hackathons"),
        ),
        migrations.AlterField(
            model_name="tool",
            name="image",
            field=models.ImageField(upload_to="tools"),
        ),
    ]
