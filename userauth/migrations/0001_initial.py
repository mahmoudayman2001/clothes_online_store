# Generated by Django 4.1.4 on 2023-03-01 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="customuser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=20)),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="profile_pic/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "USER_type",
                    models.CharField(
                        choices=[("s", "seller"), ("c", "customer")], max_length=20
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
