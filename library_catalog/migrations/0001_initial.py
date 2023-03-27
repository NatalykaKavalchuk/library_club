# Generated by Django 4.1.7 on 2023-03-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(max_length=201, unique=True, verbose_name="URL"),
                ),
                ("bio", models.TextField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        default="male-avatar-profile.jpg",
                        null=True,
                        upload_to="author_photo",
                    ),
                ),
                ("time_create", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=201,
                        null=True,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                ("description", models.TextField()),
                (
                    "poster",
                    models.ImageField(
                        blank=True,
                        default="book-image.jpg",
                        null=True,
                        upload_to="poster",
                    ),
                ),
                ("time_create", models.DateTimeField(auto_now_add=True)),
                ("time_update", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ManyToManyField(
                        related_name="books", to="library_catalog.author"
                    ),
                ),
            ],
        ),
    ]
